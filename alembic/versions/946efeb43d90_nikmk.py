"""nikmk

Revision ID: 946efeb43d90
Revises: 
Create Date: 2024-01-26 15:40:43.678723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '946efeb43d90'
down_revision: Union[str, None] = None
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
    op.create_table('lawyers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('languages', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('gendre', sa.String(length=10), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('profile_image', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lawyers_email'), 'lawyers', ['email'], unique=True)
    op.create_index(op.f('ix_lawyers_fullname'), 'lawyers', ['fullname'], unique=False)
    op.create_index(op.f('ix_lawyers_id'), 'lawyers', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('profile_image', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('appointments',
    sa.Column('appoinement_id', sa.Integer(), nullable=False),
    sa.Column('appointment_time', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lawyer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lawyer_id'], ['lawyers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('appoinement_id')
    )
    op.create_index(op.f('ix_appointments_appoinement_id'), 'appointments', ['appoinement_id'], unique=False)
    op.create_index(op.f('ix_appointments_lawyer_id'), 'appointments', ['lawyer_id'], unique=False)
    op.create_index(op.f('ix_appointments_user_id'), 'appointments', ['user_id'], unique=False)
    op.create_table('evaluations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('commentaire', sa.String(length=255), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lawyer_id', sa.Integer(), nullable=True),
    sa.Column('publication_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['lawyer_id'], ['lawyers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_evaluations_id'), 'evaluations', ['id'], unique=False)
    op.create_index(op.f('ix_evaluations_user_id'), 'evaluations', ['user_id'], unique=False)
    op.create_table('lawyer_category',
    sa.Column('Lawyer_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Lawyer_id'], ['lawyers.id'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('Lawyer_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lawyer_category')
    op.drop_index(op.f('ix_evaluations_user_id'), table_name='evaluations')
    op.drop_index(op.f('ix_evaluations_id'), table_name='evaluations')
    op.drop_table('evaluations')
    op.drop_index(op.f('ix_appointments_user_id'), table_name='appointments')
    op.drop_index(op.f('ix_appointments_lawyer_id'), table_name='appointments')
    op.drop_index(op.f('ix_appointments_appoinement_id'), table_name='appointments')
    op.drop_table('appointments')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_lawyers_id'), table_name='lawyers')
    op.drop_index(op.f('ix_lawyers_fullname'), table_name='lawyers')
    op.drop_index(op.f('ix_lawyers_email'), table_name='lawyers')
    op.drop_table('lawyers')
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_index(op.f('ix_categories_caegorie_name'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###