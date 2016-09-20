class Stark:
    creator = "George R.R. Martin"
    words = "Winter is coming"
    sigil = "Direwolf"
    home = "Winterfell"

    def __init__(self, name=None):
        self.name = name if name else "No one"

    def full_name(self):
        return "{} Stark".format(self.name)

class Lannister:
    creator = "George R.R. Martin"
    words = "Hear me roar"
    sigil = "Lion"
    home = "Casterly Rock"

    def __init__(self, name=None):
        self.name = name if name else "No one"

    def full_name(self):
        return "{} Stark".format(self.name)


class Targaryen:
    creator = "George R.R. Martin"
    words = "Fire and blood"
    sigil = "Dragon"
    home = "Valyria"

    def __init__(self, name=None):
        self.name = name if name else "No one"

    def full_name(self):
        return "{} Stark".format(self.name)
