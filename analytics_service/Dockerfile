FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE="false"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY pyproject.toml /app/
RUN poetry install --no-interaction --no-ansi --no-root

COPY . /app

EXPOSE 8001

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${PORT:-8001}"]
