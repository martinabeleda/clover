from contextlib import contextmanager
import dataclasses
import logging
from typing import List

import pandas as pd
import psycopg2

LOGGER = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class DB:
    """A class for connecting to a postgreSQL database"""

    host: str
    user: str
    password: str
    database: str
    port: int = 5432

    @contextmanager
    def managed_connection(self):
        """Acquire a managed connection to the DB

        Yields:
            A managed connection object
        """
        connection = psycopg2.connect(
            host=self.host, user=self.user, password=self.password, database=self.database, port=self.port
        )
        LOGGER.debug(f"Made connection: {connection}")
        try:
            yield connection
        finally:
            connection.close()

    def get_connection(self):
        """Acquire a connection to the DB

        Acquires a non-managed connection to the
        database. You will have to close this yourself.

        Returns:
            A connection object
        """
        connection = psycopg2.connect(
            host=self.host, user=self.user, password=self.password, database=self.database, port=self.port
        )
        LOGGER.debug(f"Made connection: {connection}")
        return connection

    def fetch_pandas_dataframe(self, sql: str) -> pd.DataFrame:
        """Fetch a `pandas.DataFrame` from the DB

        Args:
            sql (str): The query string

        Returns:
            pd.DataFrame: A `pandas.DataFrame` containing the results of the query
        """
        with self.managed_connection() as conn:
            return pd.read_sql(sql, conn)


class TransactionsDB(DB):
    """A class for connecting to the transactions database"""

    def fetch_transactions(self) -> List[dict]:
        """Fetch a list of all transactions"""
        sql = "SELECT * FROM transactions"
        df = self.fetch_pandas_dataframe(sql)
        return df.to_dict("records")

    def get_categories(self) -> List[dict]:
        """Get the available transaction categories"""
        sql = "SELECT * from categories"
        df = self.fetch_pandas_dataframe(sql)
        return df.to_dict("records")

    def get_category_types(self) -> List[dict]:
        """Get a list of category and type mappings"""
        sql = "SELECT * FROM categroy_types"
        df = self.fetch_pandas_dataframe(sql)
        return df.to_dict("records")
