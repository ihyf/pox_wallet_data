"""201907231137

Revision ID: 0f3b87e5f727
Revises: 316c22686ebf
Create Date: 2019-07-23 11:40:04.281841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f3b87e5f727'
down_revision = '316c22686ebf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
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
    sa.Column('from_address', sa.String(length=200), nullable=True),
    sa.Column('to_address', sa.String(length=200), nullable=True),
    sa.Column('tx_id', sa.String(length=400), nullable=True),
    sa.Column('in_or_out', sa.String(length=5), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('recode_logs')
    op.drop_table('account')
    # ### end Alembic commands ###
