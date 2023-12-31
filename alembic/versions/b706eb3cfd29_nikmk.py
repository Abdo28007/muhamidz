"""nikmk

Revision ID: b706eb3cfd29
Revises: a6309d37f3fd
Create Date: 2023-12-29 22:07:21.287704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b706eb3cfd29'
down_revision: Union[str, None] = 'a6309d37f3fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'evaluations', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'evaluations', 'lawyers', ['lawyer_id'], ['id'])
    op.create_foreign_key(None, 'images', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'lawyer_category', 'lawyers', ['Lawyer_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lawyer_category', 'categories', ['category_id'], ['id'], ondelete='CASCADE')
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'lawyer_category', type_='foreignkey')
    op.drop_constraint(None, 'lawyer_category', type_='foreignkey')
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    # ### end Alembic commands ###
