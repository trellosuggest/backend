from peewee import Model, CharField
from db.settings import db


class Member(Model):
    member_id = CharField(primary_key=True, max_length=512)
    full_name = CharField(max_length=128)

    class Meta:
        database = db
        table_name = 'members'
