class Kangaroo:

    pouch = []

    def __str__(self):
        return ', '.join(self.pouch)

    def __init__(self):
        self.pouch = []

    def put_in(self, object):
        self.pouch.append(str(object))

