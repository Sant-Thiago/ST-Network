from datetime import datetime
from typing import List

class STTable:
    
    def __init__(self, name: str, cols: List[str], created: datetime) -> None:
        """
        Inicializa um objeto tabela.

        :param name: nome da tabela.
        :param cols: lista de colunas.
        :param created: data de criação da tabela.
        """
        
        self.name = name
        self.cols = cols
        self.created = created

    def __repr__(self) -> str:
        return (f"STTable(name='{self.name}', "
                f"cols={self.cols}, "
                f"created={self.created})")

    def info(self) -> str:
        """
        Retorna uma string com informações sobre o objeto da tabela.
        
        :return: Informações sobre o objeto da tabela.
        """
        return (f"Tabela: {self.name}\n"
                f"Colunas: {self.cols}\n"
                f"Data de Criação: {self.created}")
    
    def insert(self, objTable) -> None:
        
        for table in objTable:
            chaves = table.keys()
            fields = ', '.join(list(chaves))
            valores = table.keys()
            values = ', '.join(list(valores))
            queries.insert(self.name, fields, values)

            


    # def getDatabases(self) -> List[STTable]:
    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute("SELECT name FROM sys.databases")
    #         databases = cursor.fetchall()