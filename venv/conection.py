import pyodbc

server = 'DESKTOP-J81F335\SQLEXPRESS'
database = 'dbBibliotecaOnline'
username = 'DESKTOP-J81F335\SQLEXPRESS'
password = '124824'
conn = pyodbc.connect(f"DRIVER={'SQL Server Native Client 11.0'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password")

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbBibliotecaOnline')
for row in cursor:
    print(row)
