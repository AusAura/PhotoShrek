"""fix rel(comment-pub) & fix-pubimg

Revision ID: b6f5f97aa155
Revises: 65de1aa50e6f
Create Date: 2024-01-14 13:23:45.535542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6f5f97aa155'
down_revision: Union[str, None] = '65de1aa50e6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pub_images', sa.Column('publication_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pub_images', 'publications', ['publication_id'], ['id'])
    op.drop_constraint('publications_pub_image_id_key', 'publications', type_='unique')
    op.drop_constraint('publications_pub_image_id_fkey', 'publications', type_='foreignkey')
    op.drop_column('publications', 'pub_image_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('pub_image_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('publications_pub_image_id_fkey', 'publications', 'pub_images', ['pub_image_id'], ['id'])
    op.create_unique_constraint('publications_pub_image_id_key', 'publications', ['pub_image_id'])
    op.drop_constraint(None, 'pub_images', type_='foreignkey')
    op.drop_column('pub_images', 'publication_id')
    # ### end Alembic commands ###
