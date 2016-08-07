class Trooper:
    job = 'Law enforcement'

    def __init__(self, name):
        self.name = name


class SuperTrooper(Trooper):

    def __init__(self, name, is_mustached):
        super().__init__(name)
        self.is_mustached = is_mustached

    def m(self):
        print(self.name)
