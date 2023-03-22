"""added users table

Revision ID: a008a2f384db
Revises: 
Create Date: 2023-03-22 18:05:10.945982

"""
from alembic import op
import sqlalchemy as sa


revision = 'a008a2f384db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('nickname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname')
    )


def downgrade() -> None:
    op.drop_table('users')
