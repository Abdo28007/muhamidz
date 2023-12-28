"""nikmk

Revision ID: 4cc854ce99ad
Revises: 72dfcc208499
Create Date: 2023-12-28 01:07:11.293585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cc854ce99ad'
down_revision: Union[str, None] = '72dfcc208499'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'evaluations', 'lawyers', ['lawyer_id'], ['id'])
    op.create_foreign_key(None, 'evaluations', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'images', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'lawyer_category', 'lawyers', ['Lawyer_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lawyer_category', 'categories', ['category_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lawyer_category', type_='foreignkey')
    op.drop_constraint(None, 'lawyer_category', type_='foreignkey')
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    # ### end Alembic commands ###