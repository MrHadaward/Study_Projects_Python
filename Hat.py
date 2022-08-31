import random

class Hat:
    contents = []

    def __init__(self, **balls):
        for key, val in balls.items():
            for add in range(val):
                self.contents.append(key)
    
    def draw(self, quantity):
        balls_taken = []

        if quantity >= len(self.contents):
            balls_taken = self.contents[:]
            self.contents.clear()
        
        else:
            for grab in range(quantity):
                grabbed = random.choice(self.contents)
                balls_taken.append(grabbed)
                self.contents.remove(grabbed)

        return balls_taken
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    green = 0
    balls_i_want = []

    for key, val in expected_balls.items():
        for rep in range(val):
            balls_i_want.append(key)

    for rep in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        hat.contents += drawn
        fail = False

        for compare in balls_i_want:
            if compare not in drawn:
                fail = True
                break
            else:
                drawn.remove(compare)

        if not fail:
            green += 1

    return green/num_experiments
