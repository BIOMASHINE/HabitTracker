"""add habit and completion models

Revision ID: 72117635fb89
Revises: 94d5443913b6
Create Date: 2026-02-16 19:22:33.362320

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "72117635fb89"
down_revision: Union[str, Sequence[str], None] = "94d5443913b6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "habits",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_habits_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_habits")),
    )
    op.create_table(
        "completions",
        sa.Column("habit_id", sa.Integer(), nullable=False),
        sa.Column(
            "completed_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["habit_id"],
            ["habits.id"],
            name=op.f("fk_completions_habit_id_habits"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_completions")),
    )


def downgrade() -> None:
    op.drop_table("completions")
    op.drop_table("habits")
