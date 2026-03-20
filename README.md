<div align="center">

# 🚀 Sistema de Cadastro de Usuários (POO ➔ API ➔ Banco de Dados)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge)](https://www.sqlalchemy.org/)

> **Uma jornada de evolução:** de uma aplicação simples de terminal (POO) para uma API REST moderna com persistência em banco de dados.

</div>

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo consolidar os fundamentos de desenvolvimento backend. A aplicação evoluiu em etapas:

1. Estruturação com **Programação Orientada a Objetos (POO)**
2. Exposição via **API REST com FastAPI**
3. Persistência de dados com **SQLite utilizando SQLAlchemy**

Agora, os dados não são mais armazenados apenas em memória — eles são persistidos em banco de dados, simulando um ambiente real de aplicações backend.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.x
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Validação de Dados:** Pydantic
* **ORM:** SQLAlchemy
* **Banco de Dados:** SQLite

---

## ✨ Funcionalidades e Evolução

### 💻 1. Versão Terminal (Core POO)
* Cadastro de usuários em memória
* Listagem e remoção por ID
* Regras de negócio isoladas

---

### 🌐 2. Versão API (FastAPI)
* CRUD completo (POST, GET, PUT, DELETE)
* Tipagem forte com Pydantic
* Geração automática de documentação (Swagger)

---

### 🗄️ 3. Persistência com Banco de Dados
* Integração com **SQLite**
* Mapeamento objeto-relacional com **SQLAlchemy (ORM)**
* Criação automática de tabelas
* Operações CRUD diretamente no banco
* Uso de sessões com Dependency Injection (`Depends`)

---

## 🔄 Endpoints da API

| Método | Rota                     | Descrição                  |
|--------|--------------------------|----------------------------|
| GET    | /Sistema-cadastro        | Listar usuários            |
| POST   | /Sistema-cadastro        | Criar novo usuário         |
| PUT    | /Sistema-cadastro/{id}   | Atualizar usuário          |
| DELETE | /Sistema-cadastro/{id}   | Deletar usuário            |

---

## 🧠 Conceitos Aplicados

Este projeto serve como prática de:

1. **Programação Orientada a Objetos (POO)**
2. **Arquitetura REST**
3. **ORM (Object Relational Mapping)**
4. **Integração com Banco de Dados**
5. **Dependency Injection no FastAPI**
6. **Boas práticas de organização de código**

---


## 📂 Arquitetura e Estrutura

sistema-cadastro/
│
├── main.py # Rotas da API (FastAPI)
├── cadastro.py # Lógica de negócio (versão POO)
├── models.py # Modelos do banco (SQLAlchemy)
├── database.py # Configuração e conexão com o banco
├── usuario.py # Schemas (Pydantic - validação de dados)
├── banco.db # Banco de dados SQLite
└── README.md

---

## ▶️ Como executar o projeto

1. Clone o repositório:

git clone https://github.com/ViniciosVicente/sistema-cadastro.git
cd sistema-cadastro

2. Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install fastapi uvicorn sqlalchemy

4. Execute a aplicação:

uvicorn main:app --reload

5. Acesse a documentação automática:

http://127.0.0.1:8000/docs

# Próximos Passos (Roadmap)

[ ] Implementar camada de segurança e autenticação com JWT.

[ ] Adicionar cobertura de testes unitários utilizando Pytest.

[ ] Criar Dockerfile e docker-compose.yml para Dockerização da aplicação.

<div align="center">
👨‍💻 Desenvolvido  por <a href="https://www.google.com/search?q=https://github.com/ViniciosVicente">Vinicios Vicente</a>.
</div>
