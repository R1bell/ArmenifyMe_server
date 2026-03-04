from __future__ import annotations

from alembic import command
from alembic.config import Config

from analytics_service.config import BASE_DIR


def main() -> None:
    config = Config(str(BASE_DIR / "alembic.ini"))
    command.upgrade(config, "head")


if __name__ == "__main__":
    main()
