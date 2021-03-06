"""empty message

Revision ID: 78445bd87a3a
Revises: e98419ea84f9
Create Date: 2019-09-19 22:49:27.243201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78445bd87a3a'
down_revision = 'e98419ea84f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('password', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('password', 'user', ['password'], unique=True)
    # ### end Alembic commands ###
