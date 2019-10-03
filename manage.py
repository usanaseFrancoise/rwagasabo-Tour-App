from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from . import db

#Creating app instance
app = create_app('development')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# manager = Manager(app)
manager.add_command('run',Server(use_debugger=True))

manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Comment = Comment, Booking = Booking, Location = Location)

@manager.command
def test():
    '''
    run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
