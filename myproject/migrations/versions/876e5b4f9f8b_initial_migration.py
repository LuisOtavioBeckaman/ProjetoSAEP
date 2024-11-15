"""Initial migration

Revision ID: 876e5b4f9f8b
Revises: 
Create Date: 2024-11-12 16:42:16.199117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '876e5b4f9f8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tarefa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=255), nullable=False),
    sa.Column('setor', sa.String(length=100), nullable=False),
    sa.Column('prioridade', sa.String(length=10), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarefa')
    op.drop_table('usuario')
    # ### end Alembic commands ###
