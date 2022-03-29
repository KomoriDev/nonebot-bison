"""add last scheduled time

Revision ID: a333d6224193
Revises: 4a46ba54a3f3
Create Date: 2022-03-29 21:01:38.213153

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a333d6224193"
down_revision = "4a46ba54a3f3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("target", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("last_schedule_time", sa.DateTime(timezone=True), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("target", schema=None) as batch_op:
        batch_op.drop_column("last_schedule_time")

    # ### end Alembic commands ###
