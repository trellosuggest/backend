from peewee import Model, ForeignKeyField
from db.settings import db
from db_model.member import Member
from db_model.board import Board


class MemberBoard(Model):
    member = ForeignKeyField(Member, related_name='member_id')
    board = ForeignKeyField(Board, related_name='board_id')

    class Meta:
        database = db
        table_name = 'member_board'
