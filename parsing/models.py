from peewee import *

from configs.settings import db


class Announcement(Model):
    image = TextField(null=True)
    price = CharField(max_length=100, null=True)
    added_at = CharField(max_length=200, null=True)
    date = CharField(max_length=20)

    class Meta:
        database = db


db.connect()
Announcement.create_table()
db.close()
