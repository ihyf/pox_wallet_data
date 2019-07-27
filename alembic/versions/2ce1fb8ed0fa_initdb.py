"""initdb

Revision ID: 2ce1fb8ed0fa
Revises: 
Create Date: 2019-07-23 10:59:46.247505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ce1fb8ed0fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recode_logs',
    sa.Column('rl_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('level_name', sa.String(length=10), nullable=True),
    sa.Column('message', sa.String(length=255), nullable=True),
    sa.Column('func_name', sa.String(length=255), nullable=True),
    sa.Column('stack_info', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('rl_id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('from_address', sa.String(length=30), nullable=True),
    sa.Column('to_address', sa.String(length=30), nullable=True),
    sa.Column('tx_id', sa.String(length=100), nullable=True),
    sa.Column('in_or_out', sa.String(length=5), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('account', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'create_time')
    op.drop_table('transactions')
    op.drop_table('recode_logs')
    # ### end Alembic commands ###