"""empty message

Revision ID: deafc30e30c
Revises: None
Create Date: 2015-06-08 15:58:12.599354

"""

# revision identifiers, used by Alembic.
revision = 'deafc30e30c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_configuration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('utility_function', sa.String(length=64), nullable=True),
    sa.Column('estimated_time', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_configuration')
    ### end Alembic commands ###