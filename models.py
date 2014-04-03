from peewee import *

database = SqliteDatabase('subvision.db', **{})

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class ActivityHotness(BaseModel):
    filepath = TextField(null=True)
    lastrevno = IntegerField(null=True)
    temperature = FloatField(null=True)

    class Meta:
        db_table = 'ActivityHotness'

class RevisionActivity(BaseModel):
    revno = IntegerField(null=True)
    temperature = FloatField(null=True)

    class Meta:
        db_table = 'RevisionActivity'

class SvnLog(BaseModel):
    addedfiles = IntegerField(null=True)
    author = TextField(null=True)
    changedfiles = IntegerField(null=True)
    commitdate = IntegerField(null=True)  # timestamp
    deletedfiles = IntegerField(null=True)
    msg = TextField(null=True)
    revno = IntegerField(null=True)

    class Meta:
        db_table = 'SVNLog'

class SvnLogDetail(BaseModel):
    changedpathid = IntegerField(null=True)
    changetype = TextField(null=True)
    copyfrompathid = IntegerField(null=True)
    copyfromrev = IntegerField(null=True)
    entrytype = CharField(null=True)
    lc_updated = CharField(null=True)
    linesadded = IntegerField(null=True)
    linesdeleted = IntegerField(null=True)
    pathtype = TextField(null=True)
    revno = IntegerField(null=True)

    class Meta:
        db_table = 'SVNLogDetail'

class Svnpaths(BaseModel):
    path = TextField(null=True)
    relpathid = IntegerField(null=True)

    class Meta:
        db_table = 'SVNPaths'
