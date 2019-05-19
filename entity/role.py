from db.settings import db
from peewee import Model, CharField, AutoField


class Role(Model):
    role_id = AutoField(primary_key=True)
    board_id = CharField(max_length=128)
    name = CharField(max_length=16)

    class Meta:
        database = db
        table_name = 'roles'
