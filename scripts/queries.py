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
