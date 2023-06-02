"""meet model

Revision ID: 8581e3e0fcdb
Revises: 3c3b13ee7432
Create Date: 2023-06-01 16:12:16.773990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8581e3e0fcdb'
down_revision = '3c3b13ee7432'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.Column('link', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meets_id'), 'meets', ['id'], unique=False)
    op.create_index(op.f('ix_meets_link'), 'meets', ['link'], unique=False)
    op.create_index(op.f('ix_meets_name'), 'meets', ['name'], unique=False)
    op.create_table('object_meet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('x', sa.Integer(), nullable=False),
    sa.Column('y', sa.Integer(), nullable=False),
    sa.Column('z_index', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.String(), nullable=False),
    sa.Column('meet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meet_id'], ['meets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_object_meet_id'), 'object_meet', ['id'], unique=False)
    op.create_index(op.f('ix_object_meet_name'), 'object_meet', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_object_meet_name'), table_name='object_meet')
    op.drop_index(op.f('ix_object_meet_id'), table_name='object_meet')
    op.drop_table('object_meet')
    op.drop_index(op.f('ix_meets_name'), table_name='meets')
    op.drop_index(op.f('ix_meets_link'), table_name='meets')
    op.drop_index(op.f('ix_meets_id'), table_name='meets')
    op.drop_table('meets')
    # ### end Alembic commands ###