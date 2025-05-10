# 2025.1-SideChef-RecipeService

## Como rodar o projeto

### Rodar o docker
docker compose up --build

### Criar ambiente virtual
```
python3 -m venv .venv
```

### Ativar ambiente
### For linux or mac
```
source .venv/bin/activate
```

### For windows
```
venv\Scripts\activate
```

### Instalar as dependências
```
pip install -r requirements.txt
```

### .env

Subistituir valores em PORT.

```
criar arquivo .env
MONGO_URI=mongodb://localhost:PORT

```

### Rodar o código
```
fastapi dev main.py
```