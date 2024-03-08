# Teste HTMLX

## Sobre o Projeto

O propósito deste projeto é explorar o uso do HTMLX, visando otimizar a renderização da página e a criação de testes unitários.

## Requisitos

- Python 3.10.5
- Django 4.0.6

## Configuração do Ambiente

1. Clone o repositório:

   `git clone https://github.com/seu_usuario/seu_projeto_django.git`

2. Crie um ambiente virtual:

   `python3 -m venv myvenv`

3. Ative o ambiente virtual:

   - No Windows:
     `myvenv\Scripts\activate`
   - No Linux/Mac:
     `source myvenv/bin/activate`

4. Instale as dependências:

   `pip install -r requirements.txt`

## Criando um Superusuário

Para criar um superusuário e acessar o painel de administração do Django:

1. Ative o ambiente virtual.
2. Execute os seguintes comandos:

   `python manage.py createsuperuser`

   _Siga as instruções para definir um nome de usuário, email e senha para o superusuário._

## Executando Migrações

1. Ative o ambiente virtual.
2. Execute o comando de migração:

   `python manage.py migrate`

## Configuração do Banco de Dados

Este projeto usa o banco de dados SQLite por padrão. Para acessar o banco de dados:

1. Ative o ambiente virtual.
2. Execute o servidor de desenvolvimento do Django:

   `python manage.py runserver`

3. Acesse o projeto no navegador em `http://127.0.0.1:8000/`.
