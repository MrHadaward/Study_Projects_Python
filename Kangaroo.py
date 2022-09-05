class Kangaroo:

    pouch = []

    def __str__(self):
        return ', '.join(self.pouch)

    def __init__(self):
        self.pouch = []

    def put_in(self, object):
        self.pouch.append(str(object))

kanga = Kangaroo()
kanga.put_in(1)

roo = Kangaroo()
roo.put_in(3)

print(kanga, roo)
