from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

# =========================
# CONFIGURAÇÕES DE SEGURANÇA
# =========================
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "unirios-sistema-chamados"),
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30),  # sessão total 30 min
    SESSION_COOKIE_HTTPONLY=True,      # cookies não acessíveis via JS
    SESSION_COOKIE_SAMESITE="Lax",     # evita CSRF básico
    SESSION_COOKIE_SECURE=False,       # trocar para True no Render (HTTPS)
    SESSION_REFRESH_EACH_REQUEST=True  # renova tempo a cada request
)

# tempo máximo de inatividade
INACTIVITY_TIMEOUT = timedelta(minutes=15)

# =========================
# CONEXÃO COM BANCO
# =========================
def conectar():
    # garante que a pasta instance exista
    os.makedirs(app.instance_path, exist_ok=True)
    db_path = os.path.join(app.instance_path, "chamados.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_banco():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        local TEXT NOT NULL,
        setor_responsavel TEXT NOT NULL,
        descricao TEXT NOT NULL,
        prioridade TEXT NOT NULL,
        status TEXT DEFAULT 'aberto',
        criado_em TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

inicializar_banco()

# =========================
# LOGIN DOS SETORES
# =========================
setores = {
    "NTI": {"usuario": "nti", "senha": "nti123"},
    "Elétrica/Clima": {"usuario": "eletrica", "senha": "eletrica123"},
    "Almoxarifado": {"usuario": "almox", "senha": "almox123"},
    "Limpeza": {"usuario": "limpeza", "senha": "limpeza123"},
    "Manutenção Predial": {"usuario": "predial", "senha": "predial123"}
}

# =========================
# DECORATOR PARA PROTEGER ROTAS
# =========================
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "usuario" not in session:
            flash("Faça login para continuar.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

# =========================
# CONTROLE DE INATIVIDADE
# =========================
@app.before_request
def enforce_session_timeout():
    if "usuario" not in session:
        return
    now = datetime.utcnow().timestamp()
    last = session.get("last_seen", now)
    if now - last > INACTIVITY_TIMEOUT.total_seconds():
        session.clear()
        flash("Sua sessão expirou por inatividade.", "info")
        return redirect(url_for("login"))
    session["last_seen"] = now

# =========================
# IMPEDIR CACHE (SEGURANÇA)
# =========================
@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0, private"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# =========================
# ROTAS PRINCIPAIS
# =========================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/novo')
def novo_chamado():
    return render_template('novo.html', setores_responsaveis=list(setores.keys()))

@app.route('/abrir', methods=['POST'])
def abrir():
    local = request.form['local']
    setor_responsavel = request.form['setor_responsavel']
    descricao = request.form['descricao']
    prioridade = request.form['prioridade']
    criado_em = datetime.now().strftime("%d/%m/%Y %H:%M")

    conn = conectar()
    c = conn.cursor()
    c.execute("""
        INSERT INTO chamados (local, setor_responsavel, descricao, prioridade, criado_em)
        VALUES (?, ?, ?, ?, ?)
    """, (local, setor_responsavel, descricao, prioridade, criado_em))
    conn.commit()
    protocolo = c.lastrowid
    conn.close()

    return redirect(url_for('sucesso', protocolo=protocolo))

@app.route('/sucesso/<int:protocolo>')
def sucesso(protocolo):
    return render_template('sucesso.html', protocolo=protocolo)

# =========================
# LOGIN / LOGOUT
# =========================
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['usuario'].strip()
        senha = request.form['senha'].strip()

        for setor, cred in setores.items():
            if cred["usuario"] == usuario and cred["senha"] == senha:
                session.clear()
                session.permanent = True  # ativa tempo total (30 min)
                session['usuario'] = usuario
                session['setor'] = setor
                session['last_seen'] = datetime.utcnow().timestamp()
                flash(f"Bem-vindo(a), {setor}!", "success")
                return redirect(url_for('painel'))

        erro = "Setor ou senha inválidos."
        flash(erro, "danger")

    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.clear()
    flash("Sessão encerrada com sucesso.", "info")
    return redirect(url_for('login'))

# =========================
# PAINEL TÉCNICO
# =========================
@app.route('/painel')
@login_required
def painel():
    setor = session.get('setor')
    status = request.args.get('status', 'aberto')

    conn = conectar()
    c = conn.cursor()
    if status == 'todos':
        c.execute("SELECT * FROM chamados WHERE setor_responsavel = ? ORDER BY id DESC", (setor,))
    else:
        c.execute("SELECT * FROM chamados WHERE setor_responsavel = ? AND status = ? ORDER BY id DESC", (setor, status))
    chamados = c.fetchall()
    conn.close()

    return render_template('painel.html', chamados=chamados, setor=setor, filtro=status)

@app.route('/alterar/<int:cid>', methods=['POST'])
@login_required
def alterar(cid):
    novo_status = request.form['status']
    conn = conectar()
    c = conn.cursor()
    c.execute("UPDATE chamados SET status = ? WHERE id = ?", (novo_status, cid))
    conn.commit()
    conn.close()
    return redirect(url_for('painel'))

# =========================
# EXECUÇÃO
# =========================
if __name__ == '__main__':
    app.run(debug=True)
