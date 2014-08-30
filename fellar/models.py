from fellar.application import app
from flask.ext.sqlalchemy import SQLAlchemy
from glask.datetimes import now
from sqlalchemy import Column, String, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

db = SQLAlchemy(app=app)

Model = db.Model


class FacebookGroup(Model):
    id = Column(String(256), primary_key=True, autoincrement=False)
    name = Column(String(512), nullable=False)


class FacebookGroupPost(Model):
    id = Column(String(256), primary_key=True, autoincrement=False)
    message = Column(Text, nullable=True)
    link = Column(String(512), nullable=True)
    group_id = Column(String(256), ForeignKey(FacebookGroup.id), nullable=False)
    group = relationship(FacebookGroup, backref='posts')
    raw = Column(JSON, nullable=False)
    created_at = Column(DateTime(True), nullable=False, default=now)
    updated_at = Column(DateTime(True), nullable=True, onupdate=now)

    @property
    def permalink(self):
        return "http://www.facebook.com/" + self.id
