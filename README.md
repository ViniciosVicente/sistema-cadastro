Sistema de Cadastro de Usuários — Python (POO + API)

Este projeto começou como um sistema de cadastro executado no terminal para praticar Programação Orientada a Objetos (POO) em Python.

Posteriormente, foi evoluído para uma API REST utilizando FastAPI, aplicando conceitos de backend e estruturação de aplicações web.

O objetivo do projeto é consolidar fundamentos antes de avançar para banco de dados e arquitetura mais robusta.

🚀 Funcionalidades
✅ Versão Terminal (POO)

Cadastro de usuários

Listagem

Remoção por ID

Geração automática de ID

Validação básica de dados

✅ Versão API (FastAPI)

CRUD completo (GET, POST, PUT, DELETE)

Validação de dados com Pydantic

Geração de UUID automático

Tratamento de erros

Documentação automática via /docs

🧠 Conceitos aplicados

Programação Orientada a Objetos

API REST

Separação de responsabilidades

Estruturação de projeto

Serialização de dados

Tratamento de exceções

Debug de problemas de tipagem

🛠 Tecnologias utilizadas

Python 3

FastAPI

Uvicorn

Pydantic

▶️ Como executar a API
1️⃣ Clonar o repositório
git clone https://github.com/ViniciosVicente/sistema-cadastro.git
cd sistema-cadastro
2️⃣ Criar ambiente virtual (opcional, recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
3️⃣ Instalar dependências
pip install fastapi uvicorn
4️⃣ Executar o servidor
uvicorn main:app --reload
5️⃣ Acessar documentação automática
http://127.0.0.1:8000/docs
📂 Estrutura do projeto
sistema-cadastro/
│
├── main.py
├── cadastro.py
├── usuario.py
└── README.md
🔮 Próximos passos

Integração com banco de dados (SQLite ou PostgreSQL)

Implementação de autenticação

Criação de testes automatizados

Deploy da API

👨‍💻 Autor

Desenvolvido por Vinicios
