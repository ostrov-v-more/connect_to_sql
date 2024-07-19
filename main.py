from sqlite3 import OperationalError
from urllib.parse import urlparse
from venv import logger

from sqlalchemy.dialects.postgresql import psycopg2

from config import DSN
# строка подключения


def dnsparser(dsn: str) -> dict[str, str]:
    pg_adress = urlparse(dsn)
    return {
        'dbname': pg_adress.path.strip('/'),
        'user': pg_adress.username,
        'password': pg_adress.password,
        'port': pg_adress.port,
        'host': pg_adress.hostname
    }

# print(dnsparser(DSN))


class SQLDeviceApi:
    def __init__(self, dns: str):
        self.conn_settings = dnsparser(dns)
        try:
            self.conn = psycopg2.connect(**self.conn_settings)
        except OperationalError as error:
            logger.error(error, exc_info=True)