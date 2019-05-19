from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'trellosuggestDB',
    user='smol',
    password='',
    host='localhost'
)
