"""empty message

Revision ID: 0254cd2e8262
Revises: 
Create Date: 2023-09-26 12:58:08.916441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0254cd2e8262'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('common_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('common_name')
    # ### end Alembic commands ###
