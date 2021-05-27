import pymysql
import random

i = 0
while i < 1000:

##3308 write 3309 read
    conection = pymysql.connect(
        host = '192.168.80.2',
        user = 'admin',
        password = 'admin',
        db = 'prueba',
        port = 3308
    )

    cursor = conection.cursor()

    #mysql = "insert into med_potencia(variable,potencia) values('23aj','4')"
    mysql = "insert into productos(costo) values(%s)"
    #Rn = "Carlos" + str(i)
    datos = random.randint(1,1000)
    #cursor.execute(mysql,datos)
    cursor.execute(mysql,datos)
    conection.commit()
    conection.close()
    i = i + 1
"""
conection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'medicion'   
)

cursor = conection.cursor()

#mysql = "insert into med_potencia(variable,potencia) values('23aj','4')"
mysql = "insert into med_potencia(variable,potencia) values(%s,%s)"
datos = ('R43224',22)
cursor.execute(mysql,datos)
conection.commit()
conection.close() """

