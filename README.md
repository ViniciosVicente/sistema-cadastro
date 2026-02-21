<div align="center">

# 🚀 Sistema de Cadastro de Usuários (POO ➔ API)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)

> **Uma jornada de evolução:** de uma aplicação simples de terminal (Orientação a Objetos) para uma API REST moderna e robusta.

</div>

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo principal consolidar os fundamentos de desenvolvimento backend. Em vez de começar direto com frameworks e bancos de dados complexos, a aplicação evoluiu em etapas: garantindo primeiro a estruturação de pacotes, manipulação de dados em memória e as regras de negócio usando POO, para só então expor essas regras através de uma API.

### 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.x
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Validação de Dados:** Pydantic

---

## ✨ Funcionalidades e Evolução

### 💻 1. Versão Terminal (Core POO)
A base do projeto, focada na lógica de negócio isolada de interfaces web.
* **Cadastro:** Registro sistemático de usuários em memória.
* **Gestão:** Listagem e remoção rigorosa baseada em IDs.
* **Lógica:** Geração automática de identificadores e validações básicas de tipos.

### 🌐 2. Versão API (FastAPI)
A camada web construída sobre o core, expondo a aplicação para o mundo.
* **CRUD Completo:** Endpoints mapeados para Criar (`POST`), Ler (`GET`), Atualizar (`PUT`) e Deletar (`DELETE`).
* **Tipagem Forte:** Uso de Pydantic para garantir a integridade dos dados (Request/Response).
* **Identificação Única:** Implementação de `UUID` para IDs seguros contra colisões e previsibilidade.
* **Docs Automáticos:** Documentação interativa e testável gerada automaticamente via Swagger UI.

---

## 🧠 Conceitos Aplicados

Este repositório serve como um laboratório prático para:

1.  **Programação Orientada a Objetos (POO):** Encapsulamento e abstração de modelos.
2.  **Arquitetura REST:** Design semântico de endpoints e uso correto dos verbos HTTP.
3.  **Clean Code:** Separação clara de responsabilidades (Rotas vs. Regras de Negócio) e tratamento de exceções.
4.  **Serialização:** Transformação fluida de objetos nativos Python para JSON.

---

## 📂 Arquitetura e Estrutura

sistema-cadastro/
├── main.py        # Ponto de entrada da API, configuração e rotas
├── cadastro.py    # Lógica de negócio e gerenciamento da base (POO)
├── models.py      # Definição das classes e esquemas de validação (Pydantic)
└── README.md      # Documentação do projeto

▶️ Como Executar o Projeto
1. Preparação do Ambiente
Bash

# 1. Clone o repositório
git clone [https://github.com/ViniciosVicente/sistema-cadastro.git](https://github.com/ViniciosVicente/sistema-cadastro.git)
cd sistema-cadastro

# 2. Crie um ambiente virtual
python -m venv .venv

# 3. Ative o ambiente virtual
# No Linux/MacOS:
source .venv/bin/activate  
# No Windows:
# .venv\Scripts\activate   
2. Instalação e Execução
Bash

# 1. Instale as dependências necessárias
pip install fastapi uvicorn pydantic

# 2. Inicie o servidor localmente
uvicorn main:app --reload
Acesse a documentação interativa da sua API em: http://127.0.0.1:8000/docs

# Próximos Passos (Roadmap)
[ ] Integrar com banco de dados relacional (SQLite/PostgreSQL) utilizando SQLAlchemy.

[ ] Implementar camada de segurança e autenticação com JWT.

[ ] Adicionar cobertura de testes unitários utilizando Pytest.

[ ] Criar Dockerfile e docker-compose.yml para Dockerização da aplicação.

<div align="center">
👨‍💻 Desenvolvido  por <a href="https://www.google.com/search?q=https://github.com/ViniciosVicente">Vinicios Vicente</a>.
</div>
