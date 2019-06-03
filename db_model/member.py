from peewee import Model, CharField
from db.settings import db


class Member(Model):
    member_id = CharField(primary_key=True, max_length=512)

    class Meta:
        database = db
        table_name = 'members'
