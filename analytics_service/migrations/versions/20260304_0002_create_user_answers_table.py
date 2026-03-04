from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260304_0002"
down_revision = "20260304_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "user_answers" in inspector.get_table_names():
        return

    op.create_table(
        "user_answers",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("word", sa.Text(), nullable=False),
        sa.Column("answer", sa.Text(), nullable=False),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_user_answers_user_id", "user_answers", ["user_id"], unique=False)


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "user_answers" not in inspector.get_table_names():
        return

    indexes = {index["name"] for index in inspector.get_indexes("user_answers")}
    if "ix_user_answers_user_id" in indexes:
        op.drop_index("ix_user_answers_user_id", table_name="user_answers")
    op.drop_table("user_answers")
