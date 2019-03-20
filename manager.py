"""
Created by Alex
"""
from app import create_app
from app.models.base import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import models

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()

