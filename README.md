# ArmenifyMe_server

## Локальный запуск

### Windows (PowerShell)

1) Создать и активировать venv:
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

2) Установить зависимости:
```powershell
pip install poetry
poetry install
```

3) Заполнить `.env` (можно скопировать из `.env.example`).

4) Применить миграции и заполнить слова:
```powershell
python manage.py migrate
python manage.py seed_words
```

5) Запуск сервера:
```powershell
python manage.py runserver
```

Swagger UI: `http://127.0.0.1:8000/api/docs/`

### Linux / macOS (bash/zsh)

1) Создать и активировать venv:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Установить зависимости:
```bash
pip install poetry
poetry install
```

3) Заполнить `.env` (можно скопировать из `.env.example`).

4) Применить миграции и заполнить слова:
```bash
python manage.py migrate
python manage.py seed_words
```

5) Запуск сервера:
```bash
python manage.py runserver
```

Swagger UI: `http://127.0.0.1:8000/api/docs/`

## Запуск через Docker

1) Убедиться, что есть `.env` (можно из `.env.example`).

2) Запуск:
```powershell
docker compose up --build
```

Swagger UI: `http://127.0.0.1:8000/api/docs/`

## Celery

### Локально

Убедись, что запущен Redis, затем:

```powershell
celery -A ArmenifyMe worker -l info
```

### Через Docker

Celery worker запускается отдельным сервисом `worker` в `docker-compose.yml`.

## Кэширование

Используется Redis cache (по умолчанию DB 1). В `.env`:

- `REDIS_CACHE_URL=redis://redis:6379/1`
- `CACHE_TTL=60`

