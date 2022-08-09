"""empty message

Revision ID: 96c36412e1e7
Revises: 
Create Date: 2022-02-27 21:42:57.135323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96c36412e1e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=100), nullable=True),
    sa.Column('skin_color', sa.String(length=100), nullable=True),
    sa.Column('eye_color', sa.String(length=100), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('vehicle_class', sa.String(length=100), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('passenger', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_favorite', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('vehicles')
    op.drop_table('users')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
