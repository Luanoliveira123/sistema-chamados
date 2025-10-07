# 🏫 Sistema de Chamados Institucionais

Um sistema web desenvolvido em **Flask (Python)** para **gerenciamento de chamados técnicos institucionais**, facilitando a comunicação entre setores de manutenção, limpeza, almoxarifado e TI.

---

## 🚀 Funcionalidades

- **Abertura de chamados** por qualquer usuário via **QR Code**  
- **Gerenciamento interno** dos chamados pelos setores responsáveis  
- **Interface responsiva** (acessível via celular ou computador)  
- **Painel técnico** com filtros de status e prioridade  
- **Sistema de login** exclusivo para técnicos  
- **Banco de dados integrado (SQLite)**  
- **Design institucional limpo e moderno**

---

## 🧠 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask Framework**
- **HTML5, CSS3, Bootstrap 5**
- **SQLite**
- **Gunicorn (para deploy)**
- **Render (para hospedagem futura)**

---

## 📱 Acesso via QR Code

O sistema foi pensado para uso prático em campo:  
qualquer usuário pode escanear um **QR Code fixado em locais estratégicos**  
e abrir um chamado direto do celular.

---

## 🧩 Estrutura de Pastas

sistema-chamados/
│
├── app.py
├── chamados.db
├── requirements.txt
├── Procfile
├── .gitignore
│
├── /static
│ ├── /css
│ ├── /img
│ └── manifest.json
│
└── /templates
├── base.html
├── index.html
├── login.html
├── novo.html
├── painel.html
└── sucesso.html

---

## 👨‍💻 Autor

**Luan de Queiroz Oliveira**  
Desenvolvido como projeto de conclusão de curso (TCC) —  
**Centro Universitário UniRios, 2025**  
Curso: *Sistemas de Informação*  

📧 *luandequeirozoliveira@gmail.com*

---

## ⚙️ Deploy (Render)

O sistema será hospedado na plataforma **Render**,  
permitindo acesso público via link institucional e QR Code.

---

## 🛠️ Licença

Este projeto é de uso **institucional e educacional**.  
Qualquer modificação ou uso comercial deve ser previamente autorizado.

