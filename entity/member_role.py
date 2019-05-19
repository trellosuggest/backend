from db.settings import db
from entity.member import Member
from entity.role import Role
from peewee import Model, ForeignKeyField, AutoField


class MemberRole(Model):
    id_ = AutoField(primary_key=True)
    member_ = ForeignKeyField(Member, related_name='member_id')
    role_ = ForeignKeyField(Role, related_name='role_id')

    class Meta:
        database = db
        table_name = 'members_roles'
