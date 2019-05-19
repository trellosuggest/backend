from db.settings import db
from entity.member import Member
from peewee import Model, CharField, ForeignKeyField, DateField, AutoField


class Log(Model):
    log_id = AutoField(primary_key=True)
    member = ForeignKeyField(Member, related_name='member_id')
    datetime = DateField()
    description = CharField(max_length=512)

    class Meta:
        database = db
        table_name = 'logs'
