class Observer:

    def __init__(self, look):
        look.add(self)

    def notify(self, look, *args, **kwargs):
        print ('Obtenido', args, kwargs, 'de', look)

class Observable:

    def __init__(self):
        self._observers = []

    def add(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def un_add(self, observer):
        self._observers.remove(observer)

subject = Observable()


observer1 = Observer(subject)
observer2 = Observer(subject)

subject.notify_observers('Este es el primer mensaje', kw='del observador')
subject.un_add(observer2)

subject.notify_observers('Este es el segundo mensaje', kw='del observador')