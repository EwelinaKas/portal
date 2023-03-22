"""rename users table to authors

Revision ID: 96effc4f5759
Revises: 05c0aaa01a62
Create Date: 2023-03-22 18:54:38.740574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96effc4f5759'
down_revision = '05c0aaa01a62'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('users', 'authors')


def downgrade() -> None:
    op.rename_table('authors', 'users')
