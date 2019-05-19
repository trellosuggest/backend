from db.settings import db
from peewee import CharField, Model, AutoField


class Member(Model):
    member_id = AutoField(primary_key=True)
    avatar_url = CharField(max_length=512)
    full_name = CharField(max_length=128)
    username = CharField(max_length=64)
    url = CharField(unique=True, max_length=512)
    roles = []

    class Meta:
        database = db
        table_name = 'members'
