
class Rectangle:

    def __repr__(self):
        inf = 'Rectangle(width={}, height={})'.format(self.width, self.height)
        return inf

    def __init__(self, wid, hei):
        self.width = None
        self.height = None
        self.set_width(wid)
        self.set_height(hei)

    def set_width(self, wid):
        self.width = wid
    
    def set_height(self, hei):
        self.height = hei

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return self.height * 2 + self.width * 2

    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        picture = ''
        for hei in range(self.height):
            picture += '*' * self.width + '\n'

        return picture
    
    def get_amount_inside(self, shape):
        fits = (self.height // shape.height) * (self.width // shape.width)
        return fits

class Square(Rectangle):
    def __str__(self):
        inf = 'Square(side={})'.format(self.height)
        return inf

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_width(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_height(self, side):
        super().set_height(side)
        super().set_width(side)

