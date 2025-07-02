FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root
#RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY banco ./banco
COPY main.py .
COPY input_model ./input_model

CMD [ "python", "main.py" ]

#docker build -t banco-app .
#docker run -it --rm banco-app
