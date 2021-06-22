from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from project import app
from project.models import User
from project import db

cli = FlaskGroup(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()
