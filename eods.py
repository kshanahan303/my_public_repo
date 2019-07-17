import cx_Oracle
import pandas as pd

connect_string = 'ora-dstgd1:1521/dstgd1.den.ofi.com'
username = 'kennis'
password = 'apppwd1'

def get_hidden():
    return 'hiwei'

def query(sql_file):
    f = open(sql_file)
    sql = f.read()
    conn = cx_Oracle.connect(username, password, connect_string)
    return pd.read_sql(sql, conn)
    

