from operator import index
import mysql.connector
import os
from turtle import title
from click import option 
from pick import pick
from datetime import datetime
from datetime import date



host= str(input("Digite host: "))
user= str(input("Digite user: "))
password=input("Digite password: ")
port=input("Digite puerto: ")

db = mysql.connector.connect(
    host=host,
    user=user,
    password="",
    port=port, # Opcional por defecto 3306
)

cursor = db.cursor()
cursor.execute('SHOW DATABASES')
db=cursor.fetchall()
os.popen("cls")

#os.popen("mysqldump -h localhost -u root testingdb > db.sql")

#restaurar copia de seguridad
#os.popen("mysql -h localhost -u root < db.sql")


title = 'Bases de datos'
options=db
option, index = pick(options, title)
print(option)
print(index)
today = date.today()
now = datetime.now()
fecha= str(today)+str(now.hour)+str(now.minute)+str(now.second)
ruta=input("¿donde desea guardar la copa de seguridad? ")
nombre = "db"
baseDatos=db[index]
nombre_sql = str(nombre+ruta+fecha+".sql")
print (str(ruta))+"'db.sql"
os.popen("mysqldump -h '"+str(host)+"' -u '" +str(user)+"' '" +str(baseDatos)+"' > '"+str(ruta)+"'db.sql")

#/C:/Users/Users/alexc/OneDrive/Escritorio (db-2022-04-05-9:42.sql)