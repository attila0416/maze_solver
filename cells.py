class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        pass

    def __repr__(self):
        return "Start({})".format(self.display)

    def __eq__(self, o) -> bool:
        return type(self) == type(o)


class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        pass

    def __eq__(self, o) -> bool:
        return type(self) == type(o)

    def __repr__(self):
        return "End({})".format(self.display)


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        pass

    def __eq__(self, o) -> bool:
        return type(self) == type(o)

    def __repr__(self):
        return "Air({})".format(self.display)


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        pass

    def __eq__(self, o: object) -> bool:
        return type(self) == type(o)

    def __repr__(self):
        return "Wall({})".format(self.display)


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        pass

    def __eq__(self, o) -> bool:
        return type(self) == type(o)

    def __repr__(self):
        return "Fire({})".format(self.display)


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        pass

    def __eq__(self, o) -> bool:
        return type(self) == type(o)

    def __repr__(self):
        return "Water({})".format(self.display)


class Teleport:
    def __init__(self, num):
        self.display = num  # You'll need to change this!

    def step(self, game):
        pass

    def __eq__(self, o) -> bool:
        return type(self) == type(o) and self.display == o.display

    def __repr__(self):
        return "Teleport({})".format(self.display)
