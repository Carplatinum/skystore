import psycopg2

try:
    # Попытка подключиться к базе данных с вашими параметрами
    conn = psycopg2.connect(
        dbname="skystore_db",
        user="skystore_user",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
