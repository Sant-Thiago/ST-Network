#!/bin/bash

/opt/mssql/bin/sqlservr &

echo "Esperando o SQL Server iniciar..."
while ! /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "st@Password@2024" -C -Q "SELECT 1" &> /dev/null
do 
    echo "Aguardando o SQL Server estar pronto..."
    sleep 5
done

echo "Executando o script de inicialização..."
/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "st@Password@2024" -C -i /usr/src/app/init-database.sql

wait
