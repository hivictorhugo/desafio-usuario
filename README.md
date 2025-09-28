# Desafio Usuário - API Flask

API simples de gerenciamento de usuários utilizando Flask, SQLAlchemy e Flask-Migrate.  
Seguindo arquitetura MVC, separando **Models**, **Services** e **Controllers**.

---

## **Funcionalidades**
- Criar usuário (POST /usuarios)
- Listar usuários (GET /usuarios)
- Estrutura MVC com separação de responsabilidades
- Banco de dados SQLite versionado com Flask-Migrate
- Respostas em JSON, códigos HTTP corretos (201, 200)

---

## **Tecnologias**
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite

---

## **Arquitetura do Projeto (MVC)**

desafio-usuario/
│
├── app/
│ ├── controllers/ # Recebe a requisição e envia para services
│ ├── services/ # Regras de negócio e manipulação do banco
│ ├── models/ # Modelos do banco (SQLAlchemy)
│ ├── init.py # Cria a app, registra blueprints e extensões
│ └── extensions.py # SQLAlchemy e Migrate
│
├── migrations/ # Versionamento do banco
├── venv/ # Ambiente virtual (não subir)
├── requirements.txt
└── README.md

yaml
Copiar código

---

## **Pré-requisitos**
- Python 3 instalado
- Git
- Ambiente virtual (venv)

---

## **Instalação**

1. Clonar o repositório:
```bash
git clone https://github.com/USERNAME/REPO.git
cd REPO
Criar e ativar o ambiente virtual:

bash
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Instalar dependências:

bash
Copiar código
pip install -r requirements.txt
Criar banco de dados com migrations:

bash
Copiar código
flask db upgrade
Executando a API
bash
Copiar código
flask run
A API estará disponível em: http://127.0.0.1:5000/

Endpoints
POST /usuarios – Criar usuário
Request body (JSON):

json
Copiar código
{
  "nome": "Victor",
  "email": "victor@ex.com"
}
Exemplo usando PowerShell:

powershell
Copiar código
Invoke-RestMethod -Uri http://127.0.0.1:5000/usuarios `
  -Method POST `
  -Body (@{nome="Victor"; email="victor@ex.com"} | ConvertTo-Json) `
  -ContentType "application/json"
Exemplo usando HTTPie:

bash
Copiar código
http POST http://127.0.0.1:5000/usuarios nome="Victor" email="victor@ex.com"
Resposta:

json
Copiar código
{
  "id": 1,
  "nome": "Victor",
  "email": "victor@ex.com"
}
GET /usuarios – Listar todos os usuários
Exemplo usando PowerShell:

powershell
Copiar código
Invoke-RestMethod -Uri http://127.0.0.1:5000/usuarios -Method GET
Exemplo usando HTTPie:

bash
Copiar código
http GET http://127.0.0.1:5000/usuarios
Resposta (se houver usuários):

json
Copiar código
[
  {"id": 1, "nome": "Victor", "email": "victor@ex.com"},
  {"id": 2, "nome": "Carlos", "email": "carlos@ex.com"}
]
Resposta (se nenhum usuário):

json
Copiar código
{
  "message": "Nenhum usuário encontrado"
}
Observações
Banco de dados SQLite local: usuarios.db (não subir no GitHub)

Pasta migrations/ incluída para versionamento do banco

instance/ e arquivos .db são locais e devem ser ignorados

Seguir sempre o fluxo MVC: Controller → Service → Model

Dicas
Para criar novas colunas ou tabelas, use Flask-Migrate:

bash
Copiar código
flask db migrate -m "Adicionando coluna X"
flask db upgrade
Sempre mantenha o requirements.txt atualizado:

bash
Copiar código
pip freeze > requirements.txt