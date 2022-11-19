# Desafio Tech (Automação) - Estágio em Automação e Desenvolvimento de Software na Frexco

O projeto consiste na resolução do desafio proposto no processo seletivo

## Funcionalidades
- Registrar usuários
- Autenticação via Token
- Listagem de usuários em formatos json, xlsx, csv
- Paginação

## Instalação

Clone o repositório e utilize a linha de comando para a instalação de todas as dependências do projeto

```bash
pip install -r requirement.txt
```

Para inicializar o banco de dados 

```bash
python manage.py migrate
```

## API endpoints

| Verbos HTTP | Endpoints | Ação | Parâmetros (Body) | Headers |
| --- | --- | --- | --- | --- |
| POST | /register | Registrar um novo usuário | username, password (opcional), birthdate (YYYY-MM-DD)| Accept: application/json |
| POST | /login | Realizar login | | Accept: application/json; Authorization: Token token_here |
| GET | /users | Consultar usuários em json | | Accept: application/json; Authorization: Token token_here |
| GET | /users/xlsx | Consultar usuários em xlsx | | Accept: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; Authorization: Token token_here
| GET | /users/csv | Consultar usuários em csv | | Accept: text/csv; Authorization: Token token_here |

## Tecnologias utilizadas

- Django
- Django Rest Framework
- SQLite