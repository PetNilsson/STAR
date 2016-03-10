from flask import url_for
from FlaskWebProject import db

class Report(db.Document):
    workDate = db.DateTimeField(required=True)
    worker = db.StringField(max_length=255, required=True)
    time = db.FloatField()

    def get_absolute_url(self):
        return url_for('report', kwargs={"id": self.id})

    def __unicode__(self):
        return self.time

    meta = {
        'allow_inheritance': True,
        'indexes': ['id', 'workDate'],
        'ordering': ['-workDate']
    }

class Right(db.EmbeddedDocument):
    system = db.StringField(max_length=255, required=True)
    read = db.BooleanField(required=True)
    write = db.BooleanField(required=True)

class User(db.Document):
    username = db.StringField(max_length=255, required=True, default='')
    password = db.StringField(max_length=255, required=True)
    firstname = db.StringField(max_length=255, default='')
    lastname = db.StringField(max_length=255, default='')
    email = db.StringField(max_length=255, default='')
    rights = db.EmbeddedDocumentListField(Right)

