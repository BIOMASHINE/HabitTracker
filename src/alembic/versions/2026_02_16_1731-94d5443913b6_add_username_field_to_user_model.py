"""add username field to user model

Revision ID: 94d5443913b6
Revises: 79a53e7d9c6c
Create Date: 2026-02-16 17:31:47.693790

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "94d5443913b6"
down_revision: Union[str, Sequence[str], None] = "79a53e7d9c6c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("username", sa.String(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_username"), "users", ["username"]
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_username"), "users", type_="unique")
    op.drop_column("users", "username")
