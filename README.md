# 🐍 AgroMercado API - Backend (Django)

Esta é a API do projeto **AgroMercado**, desenvolvida com **Django 5.2.1** e **Django REST Framework**, fornecendo endpoints seguros e performáticos para listagem, criação e exclusão de produtos agrícolas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- Django 5.2.1
- Django REST Framework
- JWT (via `rest_framework_simplejwt`) - Para autenticação rápida e moderna.
- SQLite - Banco integrado ao Django para praticidade
- Cache com LocMemCache (memória local) - Eficaz para aplicações que não visam build.

## 🔐 Autenticação JWT

A API utiliza autenticação via **JWT**:

- `POST /api/token/` – Gera token de acesso e refresh.
- `POST /api/token/refresh/` – Renova token de acesso.

Para consumir os endpoints protegidos, envie o header:

## 📦 Endpoints

| Método | Rota                     | Descrição                     | Autenticação |
|--------|--------------------------|-------------------------------|--------------|
| GET    | `/api/products`          | Lista todos os produtos       | ✅ Sim       |
| POST   | `/api/products/create`   | Cria um novo produto          | ✅ Sim       |
| DELETE | `/api/products/delete/<id>` | Remove um produto específico | ✅ Sim       |

---

## 💾 Validações de Produto

- Nome: mínimo de 3 caracteres e máximo de 20.
- Preço: mínimo R$0,01, com até 2 casas decimais.

---

## ⚙️ Cache

O endpoint de listagem de produtos é **cacheado por 10 minutos** usando o `LocMemCache` do Django.

- O cache é invalidado automaticamente ao criar ou excluir um produto.

---

## 🧪 Testes

O projeto inclui uma bateria de testes automatizados:

## 👀 Requisitos
- Python 3.12 ou superior com pip

## 🚀 Instalação e Execução
- clone o repositório: https://github.com/RyannMagalhaes/agro-mercado-server.git
- abra o prompt de comando na pasta do projeto 
- execute o comando: o comando: pip install -r requirements.txt
- execute as migrations: python manage.py migrate
- inicie a aplicacao: python manage.py runserver

O projeto inclui uma bateria de testes automatizados que pode ser rodada com:
- python manage.py test

```bash
python manage.py test

