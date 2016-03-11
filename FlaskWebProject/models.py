from flask import url_for
from FlaskWebProject import db

class Machine(db.Document):
    machineName = db.StringField(max_length=255, default='', required=True)
    owner = db.StringField(max_length=255, default='')

class MachineReport(db.EmbeddedDocument):
    machine = db.ReferenceField(Machine)
    time = db.FloatField()

class Material(db.Document):
    name = db.StringField(max_length=255, default='', required=True)
    unit = db.StringField(max_length=20, default='')

class MaterialReport(db.EmbeddedDocument):
    material = db.ReferenceField(Material)
    volume = db.FloatField()

class Report(db.Document):
    workDate = db.DateTimeField(required=True)
    worker = db.StringField(max_length=255, required=True)
    time = db.FloatField()
    timeOb = db.FloatField()
    machines = db.ListField(db.EmbeddedDocumentField(MachineReport))
    material = db.ListField(db.EmbeddedDocumentField(MaterialReport))

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
    username = db.StringField(max_length=255, required=True, default='', unique=True)
    password = db.StringField(max_length=255, required=True)
    firstname = db.StringField(max_length=255, default='')
    lastname = db.StringField(max_length=255, default='')
    email = db.StringField(max_length=255, default='')
    rights = db.ListField(db.EmbeddedDocumentField(Right))



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return password_hash==password
