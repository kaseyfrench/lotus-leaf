"""A module to handle online and offline migration configurations.

This module was generated by alembic, and has been altered to dynamically set
the value of sqlalchemy.url.
"""

from __future__ import with_statement
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# This is the Alembic Config object, which provides access to the values within
# the .ini file in use.
config = context.config

# Interpret the config file for Python logging. This line sets up loggers.
fileConfig(config.config_file_name)

# Add any model MetaData objects here for autogenerate support.
#from myapp import mymodel
#target_metadata = mymodel.Base.metadata
target_metadata = None

# Other values from the config, defined by the needs of env.py, can be acquired:
#my_important_option = config.get_main_option("my_important_option")


def run_migrations_offline():
  """Runs a migration in 'offline' mode.

  This configures the context with just a URL and not an Engine, though an
  Engine is acceptable here as well.  By skipping the Engine creation we don't
  even need a DBAPI to be available.

  Calls to context.execute() here emit the given string to the script output.
  """
  url = config.get_main_option("sqlalchemy.url")
  context.configure(
      url=url, target_metadata=target_metadata, literal_binds=True)

  with context.begin_transaction():
    context.run_migrations()


def run_migrations_online():
  """Runs a migration in 'online' mode.

  In this scenario we need to create an Engine and associate a connection with
  the context.
  """
  connectable = engine_from_config(
      config.get_section(config.config_ini_section),
      prefix='sqlalchemy.',
      poolclass=pool.NullPool)

  with connectable.connect() as connection:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
      context.run_migrations()


def set_sqlalchemy_url():
  """Sets sqlalchemy.url from command-line arguments.

  Substitutions are made for the following paramters:

    - db_type: The database type.
    - db_user: The database username.
    - db_password: The database password.
    - db_host: The database host.
    - db_port: The database port.
    - db_name: The database name.
  """
  x_args = context.get_x_argument(as_dictionary=True)
  db_type = x_args.get('db_type', 'mysql+mysqlconnector')
  db_user = x_args.get('db_user', 'uwsolar')
  db_password = x_args.get('db_password', '')
  db_host = x_args.get('db_host', 'localhost')
  db_port = x_args.get('db_port', 3306)
  db_name = x_args.get('db_name', 'uwsolar')

  if db_type == 'sqlite':
    url = '%s:///%s' % (db_type, db_host)
  else:
    url = '%s://%s:%s@%s:%d/%s' % (db_type, db_user, db_password, db_host, db_port, db_name)

  config.set_main_option('sqlalchemy.url', url)


set_sqlalchemy_url()
if context.is_offline_mode():
  run_migrations_offline()
else:
  run_migrations_online()
