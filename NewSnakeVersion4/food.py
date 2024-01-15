# food for snakes...

import random
import turtle

class Food(turtle.Turtle):

    def __init__(self, x, y, type) -> None:
        intervall = 5 # basis for hvor ofte mat skjules
        self.__type = type
        self.__visible = 10000 # hvor lenge maten vises hver gang
        self.__hidden = 0 # hvor lenge maten er skjult per gang
        self.__timer = 10000

        turtle.Turtle.__init__(self) # kaller __init__ av foreldre klassen
        self.penup()
        self.hideturtle()
        if type == 1: # vanlig type, vises alltid
            self.shape('circle')
            self.color('red')
            self.__points = 1
            
        elif type == 2: # mer sjelden
            self.shape('triangle')
            self.color('yellow')
            self.__points = 3
            self.__visible = intervall * 2
            self.__hidden = intervall

        elif type == 3: # mest sjelden
            self.shape('turtle')
            self.color('white')
            self.__points = 5
            self.__visible = intervall
            self.__hidden = intervall * 3
        
        self.speed(0)
        self.goto(x, y)
        self.showturtle()

        if self.__type != 1: # (type 1 skal ikke skjules automatisk)
            self.__timer = int(self.__hidden * (0.5 + random.random())) # forste forflytting i spillet skjer tilfeldig tid
            
    def get_type(self):
        return self.__type
    
    def get_visible(self):
        return self.__visible

    def get_hidden(self):
        return self.__hidden    
    
    def get_timer(self):
        return self.__timer

    def set_timer(self, seconds):
        self.__timer += seconds

    def reset_timer(self):
        if self.__type != 1: # (type 1 skal ikke skjules automatisk)
            self.__timer = int(self.__hidden * (0.5 + random.random())) # forste forflytting i spillet skjer tilfeldig tid

    def get_points(self):
        return self.__points
