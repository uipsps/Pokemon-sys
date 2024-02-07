import time
import random
import sys
#################################
PikachuHp = 100
CharManderHp = 100
#CharmanderMoves
#         damge chance of working    
FireBall = [30,50]
FireTunnel = [70,43]
#PikahcuMoves
#         damge chance of working
Eltracute = [40,89]
ShockWave = [100,23]
##################################
def CharsMove():
    global PikachuHp
    MoveC = input('Its CharManders Turn What Move Will You Use? \n FireBall,FireTunnel \n:')
    if MoveC == 'FireBall':
        ChanceRollC = random.randint(0,100)
        if ChanceRollC == FireBall[1] or ChanceRollC < FireBall[1]:
            PikachuHp -= FireBall[0]
            if PikachuHp == 0 or PikachuHp < 0:
                print('CharMander Wins') 
                sys.exit 
            else:
                print('CharMander Did',FireBall[0],'Damage To Pikachu Pikachus Hp is',PikachuHp,'\n')  
                PikaMove()
        else:
            print('Move Failed \n')
            PikaMove()
    elif MoveC == 'FireTunnel':
        ChanceRollF = random.randint(0,100)
        if ChanceRollF == FireTunnel[1] or ChanceRollF < FireTunnel[1]:
            PikachuHp -= FireTunnel[0]
            if PikachuHp == 0 or PikachuHp < 0:
                print('CharMander Wins') 
                sys.exit 
            else:
               print('CharMander Did',FireTunnel[0],'Damage To Pikachu Pikachus Hp is',PikachuHp,'\n') 
               PikaMove()
        else:
          print('Move Failed \n')
          PikaMove()
    else:
        print('Thats Not A Move \n')
        CharsMove()
            
########################################################################
def PikaMove():
    global CharManderHp
    MoveP = input('Its PikaChus Turn What Move Will You Use? \n Eltracute,ShockWave \n:')
    if MoveP == 'Eltracute':
        ChanceRollU = random.randint(0,100)
        if ChanceRollU == Eltracute[1] or ChanceRollU < Eltracute[1]:
           CharManderHp -=Eltracute[0] 
           if CharManderHp == 0 or CharManderHp < 0:
               print('CharMander Wins') 
               sys.exit 
           else:
            print('Pikachu Did',Eltracute[0],'Damage To CharMander CharManders Hp is',CharManderHp,'\n')  
            CharsMove()
        else:
          print('Move Failed \n')
          CharsMove()
        
    else:
        print('Thats Not A Move \n')
        PikaMove()
        

##########################################
Dywtp = input('Do You Want To Begin? \n:')
if Dywtp == 'yes':
    print('''⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥⬛⬜⬜⬜
⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜
⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜
⬛🟥🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥⬛
⬛🟥🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥🟥⬛
⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜''')
    print('↻loading')
    time.sleep(5)
    print('Done \n')
    print('CharMander VS Pikachu \n')
    CharsMove()
    
    
    
    