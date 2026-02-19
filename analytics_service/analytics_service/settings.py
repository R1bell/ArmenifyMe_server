from pathlib import Path
import os

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


def _env_list(name: str, default: list[str] | None = None) -> list[str]:
    value = os.getenv(name)
    if value is None or not value.strip():
        return list(default or [])
    return [item.strip() for item in value.split(",") if item.strip()]


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    return int(value)


def _env_str(
    name: str,
    default: str,
    aliases: tuple[str, ...] = (),
) -> str:
    for key in (name, *aliases):
        value = os.getenv(key)
        if value is not None and value.strip():
            return value.strip()
    return default

SECRET_KEY = os.getenv("ANALYTICS_SECRET_KEY", "analytics-insecure-change-me")
DEBUG = _env_bool("ANALYTICS_DEBUG", _env_bool("DEBUG", True))
ALLOWED_HOSTS = _env_list(
    "ANALYTICS_ALLOWED_HOSTS",
    _env_list("ALLOWED_HOSTS", ["127.0.0.1", "localhost"]),
)
RAILWAY_PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN")
if RAILWAY_PUBLIC_DOMAIN:
    ALLOWED_HOSTS.append(RAILWAY_PUBLIC_DOMAIN)
ALLOWED_HOSTS = list(dict.fromkeys(ALLOWED_HOSTS))

CSRF_TRUSTED_ORIGINS = _env_list(
    "ANALYTICS_CSRF_TRUSTED_ORIGINS",
    _env_list("CSRF_TRUSTED_ORIGINS", []),
)
if RAILWAY_PUBLIC_DOMAIN:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RAILWAY_PUBLIC_DOMAIN}")
CSRF_TRUSTED_ORIGINS = list(dict.fromkeys(CSRF_TRUSTED_ORIGINS))

USE_X_FORWARDED_HOST = _env_bool(
    "ANALYTICS_USE_X_FORWARDED_HOST",
    _env_bool("USE_X_FORWARDED_HOST", True),
)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = _env_bool(
    "ANALYTICS_SECURE_SSL_REDIRECT",
    _env_bool("SECURE_SSL_REDIRECT", not DEBUG),
)
SESSION_COOKIE_SECURE = _env_bool(
    "ANALYTICS_SESSION_COOKIE_SECURE",
    _env_bool("SESSION_COOKIE_SECURE", not DEBUG),
)
CSRF_COOKIE_SECURE = _env_bool(
    "ANALYTICS_CSRF_COOKIE_SECURE",
    _env_bool("CSRF_COOKIE_SECURE", not DEBUG),
)
SECURE_HSTS_SECONDS = _env_int(
    "ANALYTICS_SECURE_HSTS_SECONDS",
    _env_int("SECURE_HSTS_SECONDS", 0),
)
SECURE_HSTS_INCLUDE_SUBDOMAINS = _env_bool(
    "ANALYTICS_SECURE_HSTS_INCLUDE_SUBDOMAINS",
    _env_bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", False),
)
SECURE_HSTS_PRELOAD = _env_bool(
    "ANALYTICS_SECURE_HSTS_PRELOAD",
    _env_bool("SECURE_HSTS_PRELOAD", False),
)

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "analytics",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "analytics_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "analytics_service.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": _env_str(
            "ANALYTICS_DB_NAME",
            "analytics",
            aliases=("PGDATABASE",),
        ),
        "USER": _env_str("ANALYTICS_DB_USER", "postgres", aliases=("PGUSER",)),
        "PASSWORD": _env_str(
            "ANALYTICS_DB_PASSWORD",
            "admin",
            aliases=("PGPASSWORD",),
        ),
        "HOST": _env_str("ANALYTICS_DB_HOST", "127.0.0.1", aliases=("PGHOST",)),
        "PORT": _env_str("ANALYTICS_DB_PORT", "5432", aliases=("PGPORT",)),
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
}

CELERY_BROKER_URL = os.getenv("ANALYTICS_CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_DEFAULT_QUEUE = os.getenv(
    "ANALYTICS_CELERY_TASK_DEFAULT_QUEUE",
    os.getenv("CELERY_ANALYTICS_QUEUE", "analytics"),
)
CELERY_TASK_ROUTES = {
    "analytics.create_user": {
        "queue": os.getenv("CELERY_ANALYTICS_QUEUE", "analytics"),
    },
}
