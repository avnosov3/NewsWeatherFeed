FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install poetry
RUN poetry install

COPY ./web .

CMD ["poetry", "run", "gunicorn", "web.wsgi", "--bind", "0:8888" ]