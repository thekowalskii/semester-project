"""Created enums

Revision ID: 7fd91dcfb670
Revises: 
Create Date: 2025-02-28 22:53:03.970837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fd91dcfb670'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


user_roles_enum = sa.Enum('user', 'admin', name='user_roles')
cart_status_enum = sa.Enum('forming', 'waiting for accept', 'accepted', name='cart_status')
painting_orientation_enum = sa.Enum('portret', 'landshaft', 'square', name='painting_orientation')


def upgrade() -> None:
    user_roles_enum.create(op.get_bind(), checkfirst=True)
    cart_status_enum.create(op.get_bind(), checkfirst=True)
    painting_orientation_enum.create(op.get_bind(), checkfirst=True)


def downgrade() -> None:
    op.execute('DROP TYPE user_roles')
    op.execute('DROP TYPE cart_status')
    op.execute('DROP TYPE painting_orientation')
