import pyodbc
from scripts import queries
from datetime import datetime
from typing import List

class STTable:
    
    def __init__(self, name: str, cols: List[str], created: datetime = datetime.now()) -> None:
        """
        Inicializa um objeto tabela.

        :param name: nome da tabela.
        :param cols: lista de colunas.
        :param created: data de criação da tabela.
        """
        
        # self.create(name)
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
    
    def create(self, name) -> None:
        try:
            result = queries.createTB(name)
            print(f'[INFO] Tabela criada com sucesso: {result}')

        except pyodbc.Error as e:
            print(f'[ERROR] Não foi possível criar tabela: {e}')

    def insert(self, objTable) -> None:
        try:
            ids = []
            for table in objTable:
                fields = join_(table.keys())
                values = join_(table.values())

                res = queries.insert(self.name, fields, values)
                ids.append(res)

            print(f'[INFO] Dados inseridos com sucesso: {ids}')
        
        except pyodbc.Error as e:
            print(f'[ERROR] Não foi possível inserir dados: {e}')
            
    def list(self, objFields="*"):
        try:
            if objFields == "*":
                result = queries.listAll(self.name)
                print(f'[INFO] Dados listados com sucesso: {result}')
                return result

            for field in objFields:
                campo = field.keys()
                values = field.values()
                if campo == "nin":
                    filteredCols = join_([col for col in self.cols if all(col != val for val in values)])
                elif campo == "in":
                    filteredCols = join_([col for col in self.cols if all(col == val for val in values)])

            result = queries.list(self.name, filteredCols)
            print(f'[INFO] Dados listados com sucesso: {result}')
            return result

        except pyodbc.Error as e:
            print(f'[ERROR] Não foi possível listar dados: {e}')


def join_(object) -> str:
    return ', '.join(list(object))