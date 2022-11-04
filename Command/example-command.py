from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass

class Call:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Comando [{command_name}] no encontrado")

class Receive:
    @staticmethod
    def run_command_1():
        print("Ejecuntado comando 1")

    @staticmethod
    def run_command_2():
        print("Ejecutando comando 2")

class Command1(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()

class Command2(Command): 
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()


get = Receive()


operation1 = Command1(get)
operation2 = Command2(get)


call = Call()
call.register("1", operation1)
call.register("2", operation2)
call.execute("1")
call.execute("2")
call.execute("1")
call.execute("2")