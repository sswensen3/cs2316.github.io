class Trooper:
    job = 'Law enforcement'

    def __init__(self, name):
        self.name = name


class SuperTrooper(Trooper):

    def __init__(self, name, is_mustached):
        super().__init__(name)
        self.is_mustached = is_mustached

    # Used by print()
    def __str__(self):
        return "<{} {}>".format(self.name, ":-{" if self.is_mustached else ":-|")

    # Used by REPL
    def __repr__(self):
        return str(self)

    # Makes instances of SuperTrooper orderable
    def __lt__(self, other):
        if self.is_mustached and not other.is_mustached:
            return False
        elif not self.is_mustached and other.is_mustached:
            return True
        else:
            return self.name < other.name

if __name__=="__main__":
    sts = [SuperTrooper("Thorny", True),
           SuperTrooper("Mac", True),
           SuperTrooper("Rabbit", True),
           SuperTrooper("Farva", True),
           SuperTrooper("Foster", False)]
    print(sts)
    print(sorted(sts))
