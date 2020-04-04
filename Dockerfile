# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
FROM python:3.8.2

SHELL ["/bin/bash", "-c"]

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN poetry build \
 && pip install dist/*.whl

CMD ["transactions", "--help"]
