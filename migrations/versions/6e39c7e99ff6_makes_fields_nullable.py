"""makes fields nullable

Revision ID: 6e39c7e99ff6
Revises: fbf1d0e1bf23
Create Date: 2023-08-18 01:54:32.523724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e39c7e99ff6'
down_revision: Union[str, None] = 'fbf1d0e1bf23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###