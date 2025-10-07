<p align="center">
  <img src="https://img.shields.io/badge/Desenvolvido%20com-Flask-blue?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Projeto-UniRios%202025-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Linguagem-Python-yellow?style=for-the-badge&logo=python">
</p>

---

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

## 📱 QR Code de Acesso

Use o QR Code abaixo para acessar o sistema de chamados diretamente do celular  
(após o deploy no Render, substitua o link pelo domínio público):

<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=http://127.0.0.1:5000" alt="QR Code do Sistema">
</p>

---

## 🛠️ Licença

Este projeto é de uso **institucional e educacional**.  
Qualquer modificação ou uso comercial deve ser previamente autorizado.

