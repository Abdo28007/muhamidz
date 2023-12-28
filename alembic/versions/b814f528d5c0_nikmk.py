"""nikmk

Revision ID: b814f528d5c0
Revises: 450ef72f2e76
Create Date: 2023-12-28 00:51:14.174196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b814f528d5c0'
down_revision: Union[str, None] = '450ef72f2e76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caegorie_name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_caegorie_name'), 'categories', ['caegorie_name'], unique=False)
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.create_table('lawyer_category',
    sa.Column('Lawyer_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Lawyer_id'], ['lawyers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Lawyer_id', 'category_id')
    )
    op.drop_index('ix_categories_avocat_caegorie_name', table_name='categories_avocat', mysql_length={'caegorie_name': 250})
    op.drop_index('ix_categories_avocat_id', table_name='categories_avocat')
    op.drop_table('categories_avocat')
    op.add_column('evaluations', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('evaluations', sa.Column('lawyer_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_evaluations_user_id'), 'evaluations', ['user_id'], unique=False)
    op.create_foreign_key(None, 'evaluations', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'evaluations', 'lawyers', ['lawyer_id'], ['id'])
    op.create_foreign_key(None, 'images', 'users', ['user_id'], ['id'])
    op.add_column('lawyers', sa.Column('rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lawyers', 'rating')
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    op.drop_index(op.f('ix_evaluations_user_id'), table_name='evaluations')
    op.drop_column('evaluations', 'lawyer_id')
    op.drop_column('evaluations', 'user_id')
    op.create_table('categories_avocat',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('caegorie_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_categories_avocat_id', 'categories_avocat', ['id'], unique=False)
    op.create_index('ix_categories_avocat_caegorie_name', 'categories_avocat', ['caegorie_name'], unique=False, mysql_length={'caegorie_name': 250})
    op.drop_table('lawyer_category')
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_index(op.f('ix_categories_caegorie_name'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
