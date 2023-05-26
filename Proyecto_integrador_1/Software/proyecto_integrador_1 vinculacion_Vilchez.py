
import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Prueba!123",
 database="Proyectointegradorv01"
)
print(midb)

