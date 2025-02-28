import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
conn = cx_Oracle.connect(user="usuario", password="contraseña", dsn=dsn)

print("Conectado a Oracle")
conn.close()
