from peewee import Model, CharField
from db.settings import db


class Board(Model):
    board_id = CharField(primary_key=True, max_length=512)

    class Meta:
        database = db
        table_name = 'boards'
