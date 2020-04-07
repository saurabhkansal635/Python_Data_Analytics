# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:14:55 2019

@author: skansal
"""


import sqlalchemy
import pyodbc
import urllib
import pandas as pd

# driver = '{ODBC Driver 13 for SQL Server}'
# server =
# database =
# PORT = '1433'
# uid  =
# pwd  =
# table =
# schema =

connection_string = 'driver=%s;server=%s;PORT=%s;database=%s;uid=%s;pwd=%s;TDS_Version=%s;'%(driver,server, PORT, database, uid, pwd, TDS_Version)


#connection_string = 'DRIVER=%s;SERVER=%s;PORT=%s;DATABASE=%s;UID=%s;PWD=%s'%(driver,server,PORT, database, uid, pwd)

#print('*'*50)
#print(connection_string )
#print('*'*50)

conn = pyodbc.connect(connection_string)


# ========================================================================================
# Getting the synonym table for tags and convert the string-synonym relation to dictionary
# ========================================================================================
quoted = urllib.parse.quote_plus( connection_string )
engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
cnxn = engine.connect()
rows = cnxn.execute("SELECT name FROM sys.tables").fetchall()
#sqlalchemy.create_engine('mssql+pyodbc://', creator=conn)
synonym_table_df = pd.read_sql_table(table_name = synonym_table, con=engine, schema=schema)           
engine.dispose()

#engine = sqlalchemy.create_engine('mssql+pyodbc://user:password@server/database')