import pymssql
from config.config import STDATABASE_CONFIG as STDB

class SQLServerConnect:
    def __init__(self) -> None:
        try:
            self.connection = pymssql.connect(
                server=STDB['sqlServer'],
                user=STDB['sqlUser'],
                password=STDB['sqlPassword'],
                database=STDB['sqlDatabase']
            )
            print("[SUCCESS] Conexão com SQL Server estabelecida com sucesso!")
        except pymssql.Error as e:
            print(f"[ERROR] erro ao conectar ao SQL Server:: {e}")
            self.connection = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            print('[INFO] Conexão com SQL Server fechada.')
        

