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

