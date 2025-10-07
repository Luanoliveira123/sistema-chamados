from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "unirios-sistema-chamados"

# =========================
# CONEXÃO COM BANCO
# =========================
def conectar():
    conn = sqlite3.connect("chamados.db")
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        for setor, cred in setores.items():
            if cred["usuario"] == usuario and cred["senha"] == senha:
                session['usuario'] = usuario
                session['setor'] = setor
                return redirect(url_for('painel'))
        erro = "Setor ou senha inválidos."
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('login'))

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
def alterar(cid):
    novo_status = request.form['status']
    conn = conectar()
    c = conn.cursor()
    c.execute("UPDATE chamados SET status = ? WHERE id = ?", (novo_status, cid))
    conn.commit()
    conn.close()
    return redirect(url_for('painel'))

if __name__ == '__main__':
    app.run(debug=True)
