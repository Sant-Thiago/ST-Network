IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = "generic_database")
BEGIN
    CREATE DATABASE generic_database;
END
GO

USE generic_database;
GO


-- SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT 
--     FROM INFORMATION_SCHEMA.COLUMNS 
--         WHERE TABLE_NAME = '{name}' 
--             AND TABLE_SCHEMA = 'dbo'