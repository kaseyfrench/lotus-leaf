"""Convert data table engine from InnoDB to MyISAM.

Revision ID: b6eaa6deed84
Revises: b80fb9e8acd7
Create Date: 2017-12-30 14:11:04.007441

"""
from alembic import context
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b6eaa6deed84'
down_revision = 'b80fb9e8acd7'
branch_labels = None
depends_on = None


def upgrade():
  """Converts the data table's engine from InnoDB to MyISAM."""
  if context.config.get_main_option('db_type') != 'mysql+mysqlconnector':
    return

  conn = op.get_bind()
  conn.execute('alter table data engine=myisam')


def downgrade():
  """Converts the data table's engine from MyISAM to InnoDB."""
  if context.config.get_main_option('db_type') != 'mysql+mysqlconnector':
    return

  conn = op.get_bind()
  conn.execute('alter table data engine=innodb')
