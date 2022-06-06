"""add constraint

Revision ID: c97c445e2bdb
Revises: 0571870f5222
Create Date: 2022-03-26 19:46:50.910721

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c97c445e2bdb"
down_revision = "0571870f5222"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("subscribe", schema=None) as batch_op:
        batch_op.create_unique_constraint(
            "unique-subscribe-constraint", ["target_id", "user_id"]
        )

    with op.batch_alter_table("target", schema=None) as batch_op:
        batch_op.create_unique_constraint(
            "unique-target-constraint", ["target", "platform_name"]
        )

    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.create_unique_constraint("unique-user-constraint", ["type", "uid"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_constraint("unique-user-constraint", type_="unique")

    with op.batch_alter_table("target", schema=None) as batch_op:
        batch_op.drop_constraint("unique-target-constraint", type_="unique")

    with op.batch_alter_table("subscribe", schema=None) as batch_op:
        batch_op.drop_constraint("unique-subscribe-constraint", type_="unique")

    # ### end Alembic commands ###
