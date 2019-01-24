"""empty message

Revision ID: be62103a5fd6
Revises: 503a67df3f7f
Create Date: 2019-01-22 23:53:15.034772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be62103a5fd6'
down_revision = '503a67df3f7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('name', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'companies', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'companies', type_='unique')
    op.drop_column('companies', 'name')
    # ### end Alembic commands ###
