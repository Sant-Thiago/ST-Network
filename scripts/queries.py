from database.connector import SQLServerConnect as ConDB

def get_databases():
    return "SELECT name FROM sys.databases"

def get_tables():
    return "SELECT name FROM sys.tables"

def insert(table, fields, values):

    placeholder = ', '.join(['?'] * len(values))

    query = f"INSERT INTO {table} ({fields}) VALUES ({placeholder}); SELECT SCOPE_IDENTITY();"

    with ConDB() as conDB:
        if conDB.connection:
            cursor = conDB.connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchone()[0]
            conDB.connection.commit()
            cursor.close()
            return result
        
def listAll(table):
    
    query = f"SELECT * FROM {table};"

    with ConDB() as conDB:
        if conDB.connection:
            cursor = conDB.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        
def list(table, fields):
    query = f"SELECT {fields} FROM {table}"

    with ConDB() as conDB:
        if conDB.connection:
            cursor = conDB.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        
def createDB(name):
    query = f"""
    BEGIN
        IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{name}')
        BEGIN
            CREATE DATABASE {name}
        END

        SELECT name FROM sys.databases WHERE name = '{name}'
    END"""

    with ConDB() as conDB:
        if conDB.connection:
            cursor = conDB.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
        
def createTB(name):
    query = f"""
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[{name}]') AND type in (N'U'))
    BEGIN
        CREATE TABLE {name} (Id INT IDENTITY(1,1) PRIMARY KEY);
    END
    """

    with ConDB() as conDB:
        if conDB.connection:
            cursor = conDB.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchmany()
            cursor.close()
            return result

# SEPARAR ISSO EM OUTROS COMANDOS

# Usado para pegar o nome das colunas da tabela especificada
# SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{name}' AND TABLE_SCHEMA = 'dbo';

# Usado para pegar detalhes da tabela
# SELECT t.name, s.name, t.create_date FROM sys.tables t JOIN sys.schemas s ON t.schema_id = s.schema_id WHERE t.name = '{name}' AND s.name = 'dbo';

