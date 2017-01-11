import psycopg2


connection = psycopg2.connect(database="server", user="postgres", password="postgres", host="127.0.0.1", port="5432")
