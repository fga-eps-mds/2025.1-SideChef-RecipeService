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
Dentro do reposítório, crie um arquivo chamado `.env` e adicione as informações enviadas pelos mantenedores, ou configure a própria pelo template:

```
DOMAIN=$DOMAIN$
ENVIRONMENT=$local$
BACKEND_CORS_ORIGINS=$http://localhost:PORT$
JWT_SECRET_KEY=$JWT$
```
### 4. Execute o docker-compose up

Na pasta do repositório execute o comando:

```
docker compose up
```

### 5. Acesse a API
Para acessar a API, utilize o `localhost` na porta `8080`:

http://localhost:8080/docs

Já para acessar o bando de dados MongoDB, acesse pela porta `8081`:

http://localhost:8081
