import random as rd

#userinput
userInput = input("Press----<1>--ROCK----<2>--SCISSOR----<3>--PAPER :  ")

#all options : ROCK | PAPER | SCISSOR
option = ['ROCK','PAPER','SCISSOR']

#user varialbe
uVar = ''
PLAY = True
PLAY0 = True

#computer random
com = rd.choice(option)

#scoreboard
DRAW = 0
LOSE = 0
WIN = 0

#assign the user option
if userInput == '1':
    uVar = 'ROCK'
elif userInput == '2':
    uVar = 'SCISSOR'
elif userInput == '3':
    uVar = 'PAPER'

#main loop
while PLAY0:

    while PLAY:
        if com == uVar:
            print("MATCH DRAW !!!!!")
            DRAW += 1
            PLAY = False

        elif com == 'ROCK' and uVar == 'PAPER':
            print("YOU WIN!")
            WIN += 1
            PLAY = False

        elif com == 'ROCK' and uVar == 'SCISSOR':
            print("YOU LOSE.")
            LOSE += 1
            PLAY = False

        elif com == 'PAPER' and uVar == 'SCISSOR':
            print('YOU WIN!')
            WIN += 1
            PLAY = False

        elif com == 'PAPER' and uVar == 'ROCK':
            print('YOU LOSE.')
            LOSE += 1
            PLAY = False

        elif com == 'SCISSOR' and uVar == 'PAPER':
            print('YOU LOSE.')
            LOSE += 1
            PLAY = False

        elif com == 'SCISSOR' and uVar == 'ROCK':
            print('YOU WIN!')
            WIN += 1
            PLAY = False

    print('''<SCORE-BOARD>
    DRAW %d
    WIN  %d
    LOSE %d'''%(DRAW, WIN, LOSE))

    if userInput == 'stop' or 'STOP' or 'Stop':
        PLAY0 = False

