import copy


class Create(object):

    class Memento(object):
        def __init__(self, state1):
            self.state1 = state1

        def return_state(self):
            return self.state1

    def set_state(self, state):
        print ('Configurando estado: {0}'.format(state))
        self.state = state

    def analysis_state(self):
        print ('Analizando estado: {0}'.format(self.state))

    def save_state(self):
        print ('Guardando estado')
        return self.Memento(copy.deepcopy(self))

    def return_state(self, memento):
        self = memento.return_state()
        print ('Rertornando estado: {0}'.format(self.state))


if __name__ == '__main__':
    orig = Create()
    orig.set_state('Estado 1')
    orig.analysis_state()
    saved_state = orig.save_state()
    orig.return_state(saved_state)