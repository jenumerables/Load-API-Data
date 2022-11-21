import pyodbc 
import sqlalchemy as sa 
from sqlalchemy import create_engine 
import urllib 

  
conn = urllib.parse.quote_plus( 
    'Data Source Name=T3chServer;' 
    'Driver={SQL Server};' 
    'Server=LT-JENUMERABLES\SQLSERVER1;' 
    'Database=MSSQLDB;' 
    'Trusted_connection=yes;' 
    
) 
conx = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn)) 