from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260304_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "analytics_analyticsuser" in inspector.get_table_names():
        return

    op.create_table(
        "analytics_analyticsuser",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("username", sa.Text(), server_default="", nullable=False),
        sa.Column("email", sa.String(length=254), server_default="", nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "analytics_analyticsuser" not in inspector.get_table_names():
        return

    op.drop_table("analytics_analyticsuser")
