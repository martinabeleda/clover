# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
FROM python:3.8.2-slim-buster as build

WORKDIR /app

RUN pip install poetry==1.0.5

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root --no-dev

COPY . .

CMD ["python", "app.py"]
