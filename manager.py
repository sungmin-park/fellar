#!/usr/bin/env python
from fellar import app
from flask.ext.script import Manager

manager = Manager(app=app)
manager.run()