'''
VIDEREUTVIKLET BASERT PÅ KODE FRA: https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/

Se readme-fil for detaljer om funksjoner jeg har videreutviklet og lagt til
'''

# import required modules
from tkinter import Y
import turtle
import time
import random
import food as fd
import snakes

START_DELAY = 0.15
delay = START_DELAY
score = 0
high_score = 0
startTime = time.time()
seconds = 0
quit = False

# Standardverdier for vindusstørrelse
WIDTH_M = 800
HEIGHT_M = 600
WIDTH_S = WIDTH_M/2
HEIGHT_S = HEIGHT_M/2
WIDTH_L = WIDTH_M * 1.5
HEIGHT_L = HEIGHT_M * 1.5

# the width and height can be put as user's choice
# choice = '2' # Praktisk når jeg TESTER PROGRAMMET

# MENY før turtle-vinduet åpner
choice = input('''
    -----------
    |  SNAKE  |
    -----------
                          
    INSTRUKSJONER:
    Styr slangen med tastene ASDW
    Q stopper spillet (lukk vinduet manuelt)
               
    Poengsystem:    RØD sirkel      1 poeng
                    GUL trekant     3 poeng
                    HVIT skilpadde  5 poeng

    OPPSETT FOR SNAKE:
    1. lite vindu
    2. middels vindu
    3. stort vindu
    4. egendefinert vindu
               
    Valg: >> '''
)

width = 0
height = 0
fortsett = True
while fortsett: # Meny
    if choice == '1':
        width = WIDTH_S
        height = HEIGHT_S
        fortsett = False
    elif choice == '2':
        width = WIDTH_M
        height = HEIGHT_M
        fortsett = False
    elif choice == '3':
        width = WIDTH_L
        height = HEIGHT_L
        fortsett = False
    elif choice == '4':
        fortsett_igjen = True
        while fortsett_igjen:
            width = int(input('Skriv inn bredde: '))
            height = int(input('Skriv inn høyde: '))
            if (width < 250 or height < 250 or width > 1200 or height > 900):
                print('Bredde og høyde må være minst 250. Bredde max 1200 og høyde max 900.')
            else:
                fortsett_igjen = False
        fortsett = False
    else: choice = input('Skriv et tall mellom 1 og 4: ')


# Definere ytterkanter som x- og y-koordinater
XBORDER = width/2
YBORDER = height/2

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=width+120, height=height+120)
wn.tracer(0)

# Tegne en ramme
frame = turtle.Turtle()
frame.pen(pencolor="white", pensize=5)
frame.penup()
frame.goto(-(XBORDER+8), -(YBORDER+8))
frame.pendown()
for i in range(2):
    frame.forward(width+16)
    frame.left(90)
    frame.forward(height+16)
    frame.left(90)
frame.hideturtle()

# text on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, YBORDER-50)
pen.write("Score : 0 High Score : 0", align="center",
          font=("candara", 24, "bold"))

segments = []

# assigning key directions
def goup():
    if head.getDirection() != "down":
        head.setDirection("up")

def godown():
    if head.getDirection() != "up":
        head.setDirection("down")

def goleft():
    if head.getDirection() != "right":
        head.setDirection("left")

def goright():
    if head.getDirection() != "left":
        head.setDirection("right")

# move snake (head)
def move():
    if head.getDirection() == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.getDirection() == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.getDirection() == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.getDirection() == "right":
        x = head.xcor()
        head.setx(x + 20)

def grow(): # vekst (generalisere på sikt)
    # Adding segment
    global delay
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    if len(segments) % 2 == 0: # etter ide fra en elev
        new_segment.color("orange")  # tail colour
    else:
        new_segment.color("brown") # tail colour secondary
    new_segment.penup()
    segments.append(new_segment)
    delay -= 0.001

def scoring(food): # poeng
    global score
    global high_score
    score += food.get_points()
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, "bold"))

def moveTail():    # Forflytte halen
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

# hente tilfeldige koordinater innenfor spilleområdet
def getRndX():    
    x = random.randint(-(XBORDER - 30), (XBORDER - 30))
    return x
def getRndY():
    y = random.randint(-(YBORDER - 30), (YBORDER - 30))
    return y

# flytter enkeltobjekter (mat)
def moveFood(food):
    fortsett = True
    while fortsett:    
        x = getRndX()
        y = getRndY()
        # print('x-verdi forslag: ', x)
        # print('y-verdi forslag: ', y)

        # sjekke at maten ikke havner under slangehalen
        tryAgain = False
        for segment in segments:
            xcor = segment.xcor()
            ycor = segment.ycor()
            # MERK: mulig jeg kan bruke verdien +- 10 her?!
            if ((x+20) > xcor and (x-20) < xcor and (y+20) > ycor and (y-20) < ycor):
                tryAgain = True
                break

        # sjekk også at maten ikke er for nær slangehodet
        xcor = head.xcor()
        ycor = head.ycor()
        if ((x+20) > xcor and (x-20) < xcor and (y+20) > ycor and (y-20) < ycor):
            tryAgain = True
            break

        if tryAgain == True: # fortsett å lete etter en aktuell plass
            continue
        else:
            food.goto(x, y) # flytter maten til et ledig sted
            fortsett = False

# "Kjøkkenet": sjekker hver enkelt mat om det er på tide å gjemme/vise mat
def foodAppearance(food): 
    global seconds
    if seconds > food.get_timer(): # sammenligner spilltid med timeren fra objektet
        if food.xcor() < XBORDER: # sjekke om maten er på brettet 
            food.goto(XBORDER + 500, YBORDER + 500)
            food.set_timer(food.get_hidden()) # endrer timer med hvor lenge den skal skjules 
        else: # hvis ikke, flytt inn på brettet
            moveFood(food)
            food.set_timer(food.get_visible()) # endrer timer med hvor lenge den skal vises 

# reset mellom hver runde: flytte slangehode i midten, miste hale, poengtavle, mat tilfeldig sted
def reset():
    global score
    global delay
    global startTime
    global seconds
    delay = START_DELAY
    time.sleep(1)
    head.goto(0, 0)
    head.setDirection("Stop")

    for segment in segments:
        segment.goto(XBORDER + 500, YBORDER + 500)

    segments.clear()
    #Aktuelt å legge mat i en felles liste med objekter og for-løkke...
    for food in allFood:
        food.goto(XBORDER + 500, YBORDER + 500)  # Mat flytte seg unna vei (midlertidig)
        food.reset_timer() # resetter timer for hver food
        if food.get_type() == 1: # flytt på all mat av type 1
            moveFood(food)
    score = 0
    startTime = time.time() # resetting time
    seconds = 0
    
    pen.clear()
    pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("candara", 24, "bold"))

def quit(): # stopper/"fryser" spillet
    global quit
    quit = True

# head of the snake
head = snakes.Snakes(0, 0) # Skape slangehodet (posisjon)

# food in the game
# oppsett med variabler
t1 = 3 # antall av type 1
t2 = 2 # etc.
t3 = 1 
allFood = []
for i in range(0,t1,1): # lager mat av type tx
    allFood.append(fd.Food(getRndX(), getRndY(), 1))
for i in range(0,t2,1): # lager mat av type tx
    allFood.append(fd.Food((XBORDER + 500), (YBORDER + 500), 2)) # starter utenfor brettet
for i in range(0,t3,1): # lager mat av type tx
    allFood.append(fd.Food((XBORDER + 500), (YBORDER + 500), 3)) # starter utenfor brettet

# kontroll av slangen
wn.listen()
# merknad: case-sensitiv styring
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

wn.onkeypress(quit, "Q") # Avslutter spillet uten feilkommando (men spiller må selv lukke vinduet)

# Main Gameplay
while quit != True:
    wn.update()
    # Slangen passerer ytterkant
    if (head.xcor() > (XBORDER-10) or head.xcor() < -(XBORDER-10)
            or head.ycor() > (YBORDER-10) or head.ycor() < -(YBORDER-10)):
        reset()
     
    # Sjekker om slangens hode berører mat 
    isEaten = head.isEating(allFood) # returnerer evt. food-objekt som spises
    # ... og flytter maten
    if isinstance(isEaten, fd.Food):
        # print('Mat er spist og skal flyttes')
        isEaten.goto(XBORDER + 500, YBORDER + 500) # finner og gir nye koordinater
        # setter ny timer (hvor lenge mat skjules). Tar hensyn til gjenværende tid av timer dersom mat ikke spist
        isEaten.set_timer(seconds-isEaten.get_timer()+isEaten.get_hidden()) 
        # SJEKK at mat type 1 dukker opp etter 1 sekund
        # ELLER ta inn ny kode, f.eks. noe med
        # else:
        #    moveFood(isEaten)
        grow() # slangen vokser, på sikt GENERALISERE til hvilken slange
        scoring(isEaten) # poeng hentes fra mat-objektet
    
    # Flytt slangen og halen
    moveTail()
    move()

    # Checking for head collisions with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            reset()

    # Food disappear and reappear
    elapsed = time.time() - startTime
    tempSeconds = int(elapsed) # checking time temporarily
    if tempSeconds > seconds:
        seconds = tempSeconds # endres hvert sekund
        # print("seconds", seconds) # for DEBUGGING
        
        # check food Appearence
        for food in allFood:
            foodAppearance(food) # "Kjøkkenet": Her behandles maten :-)
       
        # Increase speed?
        if seconds % 15 == 0: # intreffer i faste intervaller
            delay = delay * 0.8 # hastighet øker (delay minker)
    
    time.sleep(delay)

wn.mainloop()