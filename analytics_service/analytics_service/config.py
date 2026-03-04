from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent


def _load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_env(BASE_DIR / ".env")


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    return int(value)


def _env_str(name: str, default: str, aliases: tuple[str, ...] = ()) -> str:
    for key in (name, *aliases):
        value = os.getenv(key)
        if value is not None and value.strip():
            return value.strip()
    return default


def _env_list(name: str, default: list[str] | None = None) -> list[str]:
    value = os.getenv(name)
    if value is None or not value.strip():
        return list(default or [])
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(frozen=True)
class Settings:
    debug: bool
    allowed_hosts: list[str]
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str
    celery_broker_url: str
    celery_result_expires: int
    celery_task_ignore_result: bool
    celery_worker_prefetch_multiplier: int
    celery_analytics_queue: str
    celery_task_default_queue: str

    @property
    def db_dsn(self) -> str:
        return (
            f"host={self.db_host} "
            f"port={self.db_port} "
            f"dbname={self.db_name} "
            f"user={self.db_user} "
            f"password={self.db_password}"
        )

    @property
    def sqlalchemy_database_url(self) -> str:
        return (
            "postgresql+psycopg://"
            f"{quote_plus(self.db_user)}:{quote_plus(self.db_password)}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings(
    debug=_env_bool("ANALYTICS_DEBUG", _env_bool("DEBUG", True)),
    allowed_hosts=_env_list(
        "ANALYTICS_ALLOWED_HOSTS",
        ["127.0.0.1", "localhost"],
    ),
    db_host=_env_str("ANALYTICS_DB_HOST", "127.0.0.1", aliases=("PGHOST",)),
    db_port=_env_str("ANALYTICS_DB_PORT", "5432", aliases=("PGPORT",)),
    db_name=_env_str("ANALYTICS_DB_NAME", "analytics", aliases=("PGDATABASE",)),
    db_user=_env_str("ANALYTICS_DB_USER", "postgres", aliases=("PGUSER",)),
    db_password=_env_str(
        "ANALYTICS_DB_PASSWORD",
        "admin",
        aliases=("PGPASSWORD",),
    ),
    celery_broker_url=os.getenv(
        "ANALYTICS_CELERY_BROKER_URL",
        "amqp://guest:guest@rabbitmq:5672//",
    ),
    celery_result_expires=_env_int("CELERY_RESULT_EXPIRES", 3600),
    celery_task_ignore_result=_env_bool("CELERY_TASK_IGNORE_RESULT", True),
    celery_worker_prefetch_multiplier=_env_int(
        "ANALYTICS_CELERY_WORKER_PREFETCH_MULTIPLIER",
        1,
    ),
    celery_analytics_queue=os.getenv("CELERY_ANALYTICS_QUEUE", "analytics"),
    celery_task_default_queue=os.getenv(
        "ANALYTICS_CELERY_TASK_DEFAULT_QUEUE",
        os.getenv("CELERY_ANALYTICS_QUEUE", "analytics"),
    ),
)
