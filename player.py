class Player:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "{0} ({1})".format(self.name, self.color)
