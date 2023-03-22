"""add hashtags table

Revision ID: 78dc5eddf2a1
Revises: d0bd647a129a
Create Date: 2023-03-22 18:36:44.555891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78dc5eddf2a1'
down_revision = 'd0bd647a129a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hashtags')
    # ### end Alembic commands ###