import pyodbc
from scripts import queries
from datetime import datetime
from STTable import STTable
from typing import List

class STDatabase:
    
    def __init__(self, name: str, created: datetime = datetime.now()) -> None:
        """
        Inicializa um objeto banco de dados.

        :param name: nome do banco de dados.
        """
        
        self.create(name)
        self.name = name
        self.tables = List[STTable]
        self.created = created

    def __repr__(self) -> str:
        return (f"STDatabase(name='{self.name}', "
                f"tables={self.tables}, "
                f"created={self.created})")

    def info(self) -> str:
        """
        Retorna uma string com informações sobre o objeto banco de dados.
        
        :return: Informações sobre o objeto banco de dados.
        """
        return (f"Database: {self.name}\n"
                f"Tabelas: {self.tables}\n"
                f"Data de Criação: {self.created}")
    
    @classmethod
    def create(self, name) -> 'STDatabase':
        try:
            result = queries.createDB(name)
            print(f'[INFO] Database criada com sucesso: {result}')

        except pyodbc.Error as e:
            print(f'[ERROR] Não foi possível criar database: {e}')
        return self    
        
    def createTable(self, name) -> None:
        try:
            result = queries.createTB(name)
            print(f'[INFO] Database criada com sucesso: {result}')

        except pyodbc.Error as e:
            print(f'[ERROR] Não foi possível criar database: {e}')
            
