"""position model

Revision ID: 0beb831423b4
Revises: d711ec555f6d
Create Date: 2023-06-01 19:57:54.963768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0beb831423b4'
down_revision = 'd711ec555f6d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=False),
    sa.Column('x', sa.Integer(), nullable=False),
    sa.Column('y', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.String(), nullable=False),
    sa.Column('muted', sa.Boolean(), nullable=False),
    sa.Column('meet_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meet_id'], ['meets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_positions_id'), 'positions', ['id'], unique=False)
    op.create_index(op.f('ix_positions_name'), 'positions', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_positions_name'), table_name='positions')
    op.drop_index(op.f('ix_positions_id'), table_name='positions')
    op.drop_table('positions')
    # ### end Alembic commands ###