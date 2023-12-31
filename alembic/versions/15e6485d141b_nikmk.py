"""nikmk

Revision ID: 15e6485d141b
Revises: afe51f018524
Create Date: 2023-12-31 04:15:44.628771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15e6485d141b'
down_revision: Union[str, None] = 'afe51f018524'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lawyer_availabilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lawyer_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['lawyer_id'], ['lawyers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lawyer_availabilities_id'), 'lawyer_availabilities', ['id'], unique=False)
    op.create_index(op.f('ix_lawyer_availabilities_lawyer_id'), 'lawyer_availabilities', ['lawyer_id'], unique=False)
    op.add_column('appointments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('appointments', sa.Column('lawyer_id', sa.Integer(), nullable=True))
    op.add_column('appointments', sa.Column('time_availability_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_appointments_lawyer_id'), 'appointments', ['lawyer_id'], unique=False)
    op.create_index(op.f('ix_appointments_time_availability_id'), 'appointments', ['time_availability_id'], unique=False)
    op.create_index(op.f('ix_appointments_user_id'), 'appointments', ['user_id'], unique=False)
    op.create_foreign_key(None, 'appointments', 'lawyers', ['lawyer_id'], ['id'])
    op.create_foreign_key(None, 'appointments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'appointments', 'lawyer_availabilities', ['time_availability_id'], ['id'])
    op.create_foreign_key(None, 'evaluations', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'evaluations', 'lawyers', ['lawyer_id'], ['id'])
    op.create_foreign_key(None, 'images', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'lawyer_category', 'categories', ['category_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'lawyer_category', 'lawyers', ['Lawyer_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lawyer_category', type_='foreignkey')
    op.drop_constraint(None, 'lawyer_category', type_='foreignkey')
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    op.drop_constraint(None, 'evaluations', type_='foreignkey')
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_index(op.f('ix_appointments_user_id'), table_name='appointments')
    op.drop_index(op.f('ix_appointments_time_availability_id'), table_name='appointments')
    op.drop_index(op.f('ix_appointments_lawyer_id'), table_name='appointments')
    op.drop_column('appointments', 'time_availability_id')
    op.drop_column('appointments', 'lawyer_id')
    op.drop_column('appointments', 'user_id')
    op.drop_index(op.f('ix_lawyer_availabilities_lawyer_id'), table_name='lawyer_availabilities')
    op.drop_index(op.f('ix_lawyer_availabilities_id'), table_name='lawyer_availabilities')
    op.drop_table('lawyer_availabilities')
    # ### end Alembic commands ###