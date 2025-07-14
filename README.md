# 2025.1-SideChef-RecipeService
## Descrição 
Este repositório visa armazenar o microsserviço RecipeService do aplicativo SideChef, responsável pela gestão dos objetos relacionados às receitas.

## Tecnologias
|||
|-----------|--------|
| __Linguagem__ | Python |
| __Backend__ | FastAPI |
| __Banco de Dados__| MongoDB |

## Como rodar o projeto

### 1. Instalar o Docker Engine

Primeiramente instale o [Docker](https://www.docker.com) no seu computador.
### 2. Clone o repositório
Clone este repositório na sua máquina.

### 3. Crie o arquivo .env
Dentro do reposítório, crie um arquivo chamado `.env` e adicione as informações enviadas pelos mantenedores, ou configure a própria pelo template incluído no arquivo `.env.example`:

```
ME_CONFIG_MONGODB_URL=mongodb://mongo:27017/
MONGO_DB_NAME=nome_do_db
MONGO_INITDB_ROOT_USERNAME=user_root
MONGO_INITDB_ROOT_PASSWORD=password_root

ME_CONFIG_MONGODB_ADMINUSERNAME=user_admin_mongo
ME_CONFIG_MONGODB_ADMINPASSWORD=password_admin_mongo

GEMINI_API_KEY=gemini_api_key
```
### 4. Execute o docker-compose up como desenvolvedor

Na pasta do repositório execute o comando:

```
docker compose --profile dev up
```

### 5. Acesse a API
Para acessar a API, utilize o `localhost` na porta `8001`:

http://localhost:8001/docs

Já para acessar o bando de dados MongoDB, acesse pela porta `8080`:

http://localhost:8080
