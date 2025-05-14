FROM python:alpine

WORKDIR /recipeservice

COPY ./requirements.txt /recipeservice/requirements.txt

RUN pip install --no-cache-dir -r /recipeservice/requirements.txt

COPY . /recipeservice

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8080"]