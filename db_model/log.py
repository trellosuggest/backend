from peewee import Model, CharField, ForeignKeyField, DateField, AutoField
from db.settings import db
from db_model.member import Member


class Log(Model):
    log_id = AutoField(primary_key=True)
    description = CharField(max_length=1024)
    date = DateField()
    member = ForeignKeyField(Member, related_name='member_id')

    class Meta:
        database = db
        table_name = 'logs'
