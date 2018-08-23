from .exceptions import CommandError


class CommandManagement:

    def __init__(self, args=None):
        self.args = args

    def execute(self):

        try:
            command = self.args[1]
        except IndexError:
            command = 'help'

        if command == 'runserver':
            from .runserver import runserver
            if len(self.args) == 3:
                host_port = self.args[2]
                runserver(host_port)
            runserver()

        if command == 'startapp':
            if len(self.args) == 2:
                raise CommandError('startapp command should have app name!')
            from .startapp import create_app
            app_name = self.args[2]
            create_app(app_name)

        if command == 'help':
            print('available command lines are \n 1. runserver \n 2. startapp')


def command_line(args=None):
    command = CommandManagement(args)
    command.execute()
