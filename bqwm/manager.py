from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from bqwm.app import create_app
from bqwm.database import db

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='cfg', required=False)
manager.add_command('db', MigrateCommand)


def main(argv=None):
    manager.run()

if __name__ == "__main__":
    main()
