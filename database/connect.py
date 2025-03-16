import psycopg2

def connection_db():
    conn = psycopg2.connect(
        dbname="the_bear",
        user="2223_iker.rivera@iticbcn.com",
        password="system",
        host="localhost",
        port=5432
    )

    return conn