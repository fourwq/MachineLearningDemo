class Hotel(object):
    def __init__(self, room, cf=1.0, br=15):
        self.room = room
        self.fc = cf
        self.br = br

    def calc_all(self, days=1):
        print(__name__)
        return (self.room*self.fc+self.br)*days


