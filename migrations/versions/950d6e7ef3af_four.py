"""four

Revision ID: 950d6e7ef3af
Revises: 191310d9e51f
Create Date: 2023-02-26 00:34:06.423175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950d6e7ef3af'
down_revision = '191310d9e51f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('privacy', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('privacy')

    # ### end Alembic commands ###
