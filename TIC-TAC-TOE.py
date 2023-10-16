from os import system

fe=[1337,0,0,0,0,0,0,0,0,0]

def board(v, p):
    global fe
    global winner
    fe[int(v)]=p

    system('cls')
    print(str(fe[1]) +"│"+ str(fe[2]) +"│"+ str(fe[3]))
    print(str(fe[4]) +"│"+ str(fe[5]) +"│"+ str(fe[6]))
    print(str(fe[7]) +"│"+ str(fe[8]) +"│"+ str(fe[9]))
    winner=check()

def check():
    global w
    if fe[1] == fe[2] and fe[1] ==fe[3]:
        if int(fe[1]) >0:
            w=1
            return fe[1]
    elif fe[4] == fe[5] and fe[4] ==fe[6]:
        if int(fe[4]) >0:
            w=1
            return fe[4]
    elif fe[7] == fe[8] and fe[7] ==fe[9]:
        if int(fe[7]) >0:
            w=1
            return fe[7]
    if fe[1] == fe[4] and fe[1] ==fe[7]:
        if int(fe[1]) >0:
            w=1
            return fe[1]
    if fe[2] == fe[5] and fe[2] ==fe[8]:
        if int(fe[2]) >0:
            w=1
            return fe[2]
    if fe[3] == fe[6] and fe[3] ==fe[9]:
        if int(fe[3]) >0:
            w=1
            return fe[3]
    elif fe[1] == fe[5] and fe[1] ==fe[9]:
        if int(fe[1]) >0:
            w=1
            return fe[1]
    elif fe[3] == fe[5] and fe[3] ==fe[7]:
        if int(fe[3]) >0:
            w=1
            return fe[3]
    elif fe[2] == fe[5] and fe[2] ==fe[8]:
        if int(fe[2]) >0:
            w=1
            return fe[2]

board("0","0")

w=0
whichplayer=0

while w<1:
    whichplayer=whichplayer+1
    if whichplayer==3:
        whichplayer = 1

    print("Spieler"+str(whichplayer)+" ist dran.")

    richtig=True
    while richtig:
        zug=input()
        try:
            if fe[int(zug)] == 0:
                if int(zug) < 10:
                    board(zug, str(whichplayer))
                    richtig=False
            else:
                print("Dieses Feld wurde bereits besetzt")
        except:
            print("Ungültige Eingabe")

print("Spieler "+winner+" hat gewonnen.")
input()