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
    BEGIN
        IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[{name}]') AND type in (N'U'))
        BEGIN
            CREATE DATABASE {name} (Id INT IDENTITY(1,1) PRIMARY KEY);
        END

        SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[{name}]') AND type in (N'U')
    END"""

    with ConDB() as conDB:
        if conDB.connection:
            cursor = conDB.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
