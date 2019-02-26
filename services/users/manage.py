# services/users/manage.py


from flask.cli import FlaskGroup

from services.users.project import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()