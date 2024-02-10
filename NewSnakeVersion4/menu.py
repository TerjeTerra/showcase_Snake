# Menu (in terminal)
# [might be changed to a graphical interface in future version]

startMenu = '''
    -----------
    |  SNAKE  |
    -----------
                            
    INSTRUKSJONER:
        - Styr slangen med tastene ASDW eller piltastene
        - Ikke treff kantene eller deg selv (slangen din)
        - Spis mat og tjen poeng:
                
                ROED sirkel     1 poeng
                GUL trekant     3 poeng
                HVIT skilpadde  5 poeng

        - Trykk Q for aa pause spillet (SHIFT + Q for aa avslutte)
          
    HVOR STORT BRETT VIL DU SPILLE MED?:
        1. lite
        2. middels
        3. stort
        '''        

playerOptions = '''
    HVOR MANGE SPILLERE SKAL SPILLE?
        1. 1 spiller
        2. 2 spillere
        '''


def choose():
    return input("Ditt valg: ")

def newChoice():
    print('Velg et tall fra menyen (+ Enter). Tallet 0 viser menyen igjen. ')

def menuLoop(text, nrOfChoices):

    def valid(ch):
        if int(ch) in range(1, nrOfChoices + 1):
            return True
        return False
    
    print(text)
    fortsett = True
    while fortsett:
        choice = choose()
        if choice == '0':
            print(text)
            continue
        elif not valid(choice):
            newChoice()
        else:
            fortsett = False
    return choice
