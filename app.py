import mysql.connector

# Conexion a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306, # Opcional por defecto 3306
    database="blog", # Opcional
)

#Cursor para ejecutar consultas
cursor = db.cursor()

cursor.execute("show tables")

tables = cursor.fetchall()

db.commit()
cursor.close()

print(tables)


