from threading import Thread
import pymysql
import time

def MySql1():
    servidor_ip = 'localhost'
    usuario = 'root'
    contras = ''
    BD = 'numeros'
    db = pymysql.connect(host = servidor_ip, user = usuario, password=contras,
                     database = BD, charset ='utf8', 
                     cursorclass=pymysql.cursors.DictCursor)
    
    cursor = db.cursor()
    consulta = "SELECT * FROM numeros WHERE numeros <= 25"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    for i in datos:
        print(i['numeros'])

def MySql2():
    servidor_ip = 'localhost'
    usuario = 'root'
    contras = ''
    BD = 'numeros'
    db = pymysql.connect(host = servidor_ip, user = usuario, password=contras,
                     database = BD, charset ='utf8', 
                     cursorclass=pymysql.cursors.DictCursor)
    
    cursor = db.cursor()
    consulta = "SELECT * FROM numeros WHERE numeros BETWEEN 26 and 50"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    for i in datos:
        print(i['numeros'])

def MySql3():
    servidor_ip = 'localhost'
    usuario = 'root'
    contras = ''
    BD = 'numeros'
    db = pymysql.connect(host = servidor_ip, user = usuario, password=contras,
                     database = BD, charset ='utf8', 
                     cursorclass=pymysql.cursors.DictCursor)
    
    cursor = db.cursor()
    consulta = "SELECT * FROM numeros WHERE numeros BETWEEN 51 and 75"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    for i in datos:
        print(i['numeros'])

def MySql4():
    servidor_ip = 'localhost'
    usuario = 'root'
    contras = ''
    BD = 'numeros'
    db = pymysql.connect(host = servidor_ip, user = usuario, password=contras,
                     database = BD, charset ='utf8', 
                     cursorclass=pymysql.cursors.DictCursor)
    
    cursor = db.cursor()
    consulta = "SELECT * FROM numeros WHERE numeros BETWEEN 76 and 100"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    for i in datos:
        print(i['numeros'])

if __name__ == "__main__":
    print("Hilo 1")
    t = Thread(target=MySql1)
    t.start();
    
    time.sleep(2)

    print("\nHilo 2")
    t = Thread(target=MySql2)
    t.start();

    time.sleep(2)

    print("\nHilo 3")
    t = Thread(target=MySql3)
    t.start();

    time.sleep(2)

    print("\nHilo 4")
    t = Thread(target=MySql4)
    t.start();