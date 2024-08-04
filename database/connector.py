import pyodbc
from config.config import STDATABASE_CONFIG as STDB

class SQLServerConnect:
    def __init__(self) -> None:
        try:
            conn_str = (
                f"DRIVER={STDB['sqlDriver']};"
                f"SERVER={STDB['sqlServer']};"
                f"UID={STDB['sqlUser']};"
                f"PWD={STDB['sqlPassword']}"
            )

            self.connection = pyodbc.connect(conn_str)
            print("[SUCCESS] Conexão com SQL Server estabelecida com sucesso!")

        except pyodbc.Error as e:
            print(f"[ERROR] erro ao conectar ao SQL Server:: {e}")
            self.connection = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            print('[INFO] Conexão com SQL Server fechada.')

