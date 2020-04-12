from sqlalchemy import event
from sqlalchemy.engine import Engine


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Set-up Foreign Key support in SQLite

    .. _SQLAlchemy:
        https://docs.sqlalchemy.org/en/13/dialects/sqlite.html#foreign-key-support

    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
