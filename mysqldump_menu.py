from operator import index
import mysql.connector
import os
from turtle import title
from click import option 
from pick import pick
from datetime import datetime
from datetime import date
import json


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

#os.popen("mysqldump -h localhost -u root testingdb > db.sql")

#restaurar copia de seguridad
#os.popen("mysql -h localhost -u root < db.sql")


title = 'Bases de datos'
options=db
option, index = pick(options, title)
option= "".join(map(str, option))
#print(json.dumps(option))
today = date.today()
now = datetime.now()
fecha= str(today)+str(now.hour)+str(now.minute)+str(now.second)
os.system("cls")
ruta=input("¿Ingrese ruta donde guardar la copia de seguridad? ")
nombre = "db"
baseDatos=option
nombre_sql = str(ruta+ "/"+fecha+".sql")
os.popen("mysqldump -h "+str(host)+ " -u " +str(user)+ " "+option+" > "+str(nombre_sql)+"")

print("Se ha guardado la base de datos")

#Restaurar

restaurar= int(input("""¿Restaurar?
1. SI
2. NO
"""))
if restaurar == 1:
    os.system("cls")
    title = 'Seleccione base de datos para la restauracion'
    options=db
    option, index = pick(options, title)
    option= "".join(map(str, option))
    nombrebd=input("Ingrese nombre de la base de datos de respaldo: ")
    ruta=input("Ingrese ruta de la base de datos: ")
    nombre_sql=str(ruta)+str("/"+nombrebd)
    os.popen("mysql -u " +str(user)+ " "+option+" < "+str(nombre_sql)+"")

#os.popen("mysql -u root recuperaciondb < /Users/alexc/OneDrive/Escritorio/2022-05-11153857.sql")

#/C:/Users/Users/alexc/OneDrive/Escritorio (db-2022-04-05-942.sql)

#mysqldump -h localhost -u root test > /Users/alexc/OneDrive/Escritorio/db-2022-04-05-942.sql
