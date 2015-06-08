from flask.ext.script import Manager

from bqwm.app import create_app

manager = Manager(create_app())


@manager.command
def hello():
    print "Hello!"


@manager.command
def start():
    print "Start!"


def main(argv=None):
    manager.run()

if __name__ == "__main__":
    main()
