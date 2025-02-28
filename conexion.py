import cx_Oracle
""""
Al conectar con una base de datos Oracle, se establece una sesión con el servidor
a través del puerto configurado,
lo que permite el flujo de información entre el cliente y la base de datos. Python 
facilita esta conexión mediante 
el módulo cx_Oracle, que actúa como un driver para interactuar con Oracle Database
utilizando su API nativa
""""
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
conn = cx_Oracle.connect(user="usuario", password="contraseña", dsn=dsn)

print("Conectado a Oracle")
conn.close()
