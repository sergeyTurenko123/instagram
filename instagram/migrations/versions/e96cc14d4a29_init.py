"""Init

Revision ID: e96cc14d4a29
Revises: 2f6ca3767a65
Create Date: 2024-08-22 23:48:35.755297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e96cc14d4a29'
down_revision: Union[str, None] = '2f6ca3767a65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('quote', 'author',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('quote_author_fkey', 'quote', type_='foreignkey')
    op.create_foreign_key(None, 'quote', 'author', ['author'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quote', type_='foreignkey')
    op.create_foreign_key('quote_author_fkey', 'quote', 'author', ['author'], ['id'], ondelete='CASCADE')
    op.alter_column('quote', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
