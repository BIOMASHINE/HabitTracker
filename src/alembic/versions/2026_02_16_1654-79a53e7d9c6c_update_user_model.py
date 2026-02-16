"""update user model

Revision ID: 79a53e7d9c6c
Revises: 8e6b5e2f5bf5
Create Date: 2026-02-16 16:54:18.807606

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "79a53e7d9c6c"
down_revision: Union[str, Sequence[str], None] = "8e6b5e2f5bf5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "created_at")
