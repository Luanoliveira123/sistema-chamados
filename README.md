<p align="center">
  <img src="https://img.shields.io/badge/Desenvolvido%20com-Flask-blue?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Projeto-UniRios%202025-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Linguagem-Python%203.12-yellow?style=for-the-badge&logo=python">
</p>

---

# 🏫 Sistema de Chamados Institucionais — 2025

Um sistema web desenvolvido em **Flask (Python)** para **gerenciamento de chamados técnicos institucionais**, promovendo agilidade, transparência e eficiência entre setores de manutenção, limpeza, almoxarifado e TI.

---

## 🚀 Funcionalidades

- ✅ **Abertura de chamados online** por qualquer usuário (via QR Code)
- 🛠️ **Gerenciamento interno** pelos setores responsáveis
- 💻 **Interface responsiva e moderna** (Bootstrap 5)
- 🔐 **Sistema de login seguro por setor**
- 📊 **Dashboard com gráficos dinâmicos** (Chart.js)
- 💾 **Geração de backup em Excel (.xlsx)**
- ☁️ **Hospedagem em nuvem — Render (Free Tier)**

---

## 🧠 Tecnologias Utilizadas

| Tecnologia | Função Principal |
|-------------|------------------|
| **Python 3.12** | Linguagem base |
| **Flask 3.1.2** | Framework web principal |
| **SQLite** | Banco de dados leve e embutido |
| **Bootstrap 5** | Interface responsiva e institucional |
| **Chart.js** | Gráficos dinâmicos no dashboard |
| **OpenPyXL** | Exportação de relatórios para Excel |
| **Gunicorn** | Servidor de produção (usado no Render) |

---

## 🧩 Estrutura de Pastas


sistema-chamados/
│
├── app.py
├── requirements.txt
├── Procfile
├── chamados.db
│
├── /templates
│ ├── base.html
│ ├── index.html
│ ├── login.html
│ ├── novo.html
│ ├── painel.html
│ ├── sucesso.html
│ └── dashboard.html
│
└── /static
├── style.css
├── /img
└── manifest.json

---


## ⚙️ Execução Local (modo desenvolvedor)

```bash
# 1️⃣ Clonar o projeto
git clone https://github.com/luandequeiroz/sistema-chamados.git
cd sistema-chamados

# 2️⃣ Criar ambiente virtual (Python 3.12)
python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Linux/Mac)

# 3️⃣ Instalar dependências
pip install -r requirements.txt

# 4️⃣ Executar o servidor Flask
python app.py

---

## 👨‍💻 Autor

**Luan de Queiroz Oliveira**  
Desenvolvido como projeto de conclusão de curso (TCC) —  
**Sistema desenvolvido para uso corporativo e institucional, 2025**  
Curso: *Sistemas de Informação*  

📧 *luandequeirozoliveira@gmail.com*

---

## ⚙️ Deploy (Render)

☁️ Deploy Gratuito no Render

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

Este projeto é de uso **institucional e acadêmico**.  
Qualquer modificação ou uso comercial deve ser previamente autorizado.

