"""Add parent folder fk

Revision ID: d253418f7ee0
Revises: e154a0e8e33b
Create Date: 2025-01-03 17:25:34.043667

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d253418f7ee0"
down_revision: Union[str, None] = "e154a0e8e33b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("folder", sa.Column("parent_folder", sa.Uuid(), nullable=True))
    op.create_foreign_key(None, "folder", "folder", ["parent_folder"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "folder", type_="foreignkey")
    op.drop_column("folder", "parent_folder")
    # ### end Alembic commands ###
