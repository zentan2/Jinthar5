"""users table, portfolio table

Revision ID: 22697bb9130f
Revises: 
Create Date: 2022-08-15 14:20:55.389145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22697bb9130f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Ticker', sa.String(length=20), nullable=False),
    sa.Column('Quantity', sa.Integer(), nullable=False),
    sa.Column('Price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('Name', sa.String(length=200), nullable=False),
    sa.Column('Country', sa.String(length=50), nullable=False),
    sa.Column('MarketValue', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('UnrealisedPnL', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('UnrealisedPnLPercentage', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('portfolio')
    # ### end Alembic commands ###