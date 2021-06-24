"""empty message

Revision ID: 5105722022b5
Revises: 
Create Date: 2021-06-21 11:43:02.194819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5105722022b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###
    
    op.execute('UPDATE todo SET completed = False WHERE completed is NULL;')
    op.alter_column('todo','completed',nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'completed')
    # ### end Alembic commands ###
