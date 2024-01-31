import psycopg2 as psql
def connect_db(database):
    postgresconn = psql.connect(
        host = "localhost",
        database = database,
        user = "postgres",
        password = "bekzodbek"
    )
    return postgresconn


postgres_conn = connect_db("e_commerce")

