import pymysql
"""
##3308 write 3309 read
conection = pymysql.connect(
    host = '192.168.80.2',
    user = 'admin',
    password = 'admin',
    db = 'prueba',
    port = 3309
)

cursor = conection.cursor()

#mysql = "insert into med_potencia(variable,potencia) values('23aj','4')"
mysql = "select *  from productos"
#Rn = "Carlos" + str(i)
#datos = (Rn)
#cursor.execute(mysql,datos)
cursor.execute(mysql)
conection.commit()
conection.close()

print(cursor.fetchall())

##
"""
i = 0
while i < 1000:
    conection = pymysql.connect(
    host = '192.168.80.2',
    user = 'admin',
    password = 'admin',
    db = 'prueba',
    port = 3309
    )

    cursor = conection.cursor()

    #mysql = "insert into med_potencia(variable,potencia) values('23aj','4')"
    mysql = "select *  from productos"
    #Rn = "Carlos" + str(i)
    #datos = (Rn)
    #cursor.execute(mysql,datos)
    cursor.execute(mysql)
    conection.commit()
    conection.close()

    print(cursor.fetchall())
    i = i +1
