"""add_repo_notice

Revision ID: b245fbdbf730
Revises: 772c77c15667
Create Date: 2021-04-26 18:17:06.957639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b245fbdbf730'
down_revision = '772c77c15667'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('repo_notice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('repo_identifier', sa.String(length=254), nullable=False),
    sa.Column('start_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('end_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('is_warning', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repo_notice')
    # ### end Alembic commands ###
