"""nikmk

Revision ID: 450ef72f2e76
Revises: 
Create Date: 2023-12-27 20:50:15.070052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '450ef72f2e76'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_filename'), 'images', ['filename'], unique=False)
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    op.drop_index('ix_categories_avocat_caegorie_name', table_name='categories_avocat', mysql_length={'caegorie_name': 250})
    op.drop_index('ix_categories_avocat_id', table_name='categories_avocat')
    op.drop_table('categories_avocat')
    op.drop_index('ix_appointments_id', table_name='appointments')
    op.drop_table('appointments')
    op.drop_index('ix_evaluations_id', table_name='evaluations')
    op.drop_table('evaluations')
    op.drop_index('ix_lawyers_email', table_name='lawyers')
    op.drop_index('ix_lawyers_fullname', table_name='lawyers', mysql_length={'fullname': 250})
    op.drop_index('ix_lawyers_id', table_name='lawyers')
    op.drop_table('lawyers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lawyers',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('fullname', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('languages', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('gendre', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('phone_number', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_lawyers_id', 'lawyers', ['id'], unique=False)
    op.create_index('ix_lawyers_fullname', 'lawyers', ['fullname'], unique=False, mysql_length={'fullname': 250})
    op.create_index('ix_lawyers_email', 'lawyers', ['email'], unique=True)
    op.create_table('evaluations',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('commentaire', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('rating', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('publication_date', sa.DATE(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_evaluations_id', 'evaluations', ['id'], unique=False)
    op.create_table('appointments',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('appointment_time', mysql.DATETIME(), nullable=True),
    sa.Column('accepted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.create_index('ix_appointments_id', 'appointments', ['id'], unique=False)
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
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_index(op.f('ix_images_filename'), table_name='images')
    op.drop_table('images')
    # ### end Alembic commands ###
