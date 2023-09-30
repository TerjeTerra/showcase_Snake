# Kode som utgangpunkt for klasse med slanger.
# Foreløpig bare kode for hodet, ikke hale

import turtle

class Snakes(turtle.Turtle):
    
    def __init__(self, x, y) -> None:
        self.direction = "Stop"
        
        # self.__type = type # Player eller datastyrt   
        #colors = random.choice(['red', 'green', 'black'])
        #shapes = random.choice(['square', 'triangle', 'circle'])

        turtle.Turtle.__init__(self) 
        self.penup()
        self.hideturtle()
        self.shape('square')
        self.color("white")
        self.speed(0)
        self.goto(x, y)
        self.showturtle()

    def getDirection(self):
        return self.direction
    
    def setDirection(self, direction):
        self.direction = direction

    def isEating(self, allFood): # sjekker om slangen spiser
        for food in allFood:
            if self.distance(food) < 20:
                # print('SPISER')
                return food
   

