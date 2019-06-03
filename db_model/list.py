from peewee import Model, CharField, ForeignKeyField, BooleanField
from db.settings import db
from db_model.board import Board


class List(Model):
    list_id = CharField(primary_key=True, max_length=512)
    is_ignored = BooleanField()
    board = ForeignKeyField(Board, related_name='board_id')

    class Meta:
        database = db
        table_name = 'lists'
