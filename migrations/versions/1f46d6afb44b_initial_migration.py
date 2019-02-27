"""Initial Migration

Revision ID: 1f46d6afb44b
Revises: d4086115876f
Create Date: 2019-02-26 17:48:30.168080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f46d6afb44b'
down_revision = 'd4086115876f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('narration', sa.String(length=400), nullable=True))
    op.drop_column('pitches', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'narration')
    # ### end Alembic commands ###
