import pygame
import os

from board import chessBoard
from board.move import Move
from player.minimax import Minimax
from playsTree import DesicionTree


#initiate tree
tree = DesicionTree(3)


pygame.init()
gameDisplay = pygame.display.set_mode((1100, 825))
pygame.display.set_caption("PyChess")
clock = pygame.time.Clock()
firstBoard = chessBoard.Board()
firstBoard.createBoard('TableroDeJuego')
#firstBoard.printBoard()

allTiles = []
allPieces = []
ActionsList = []
axis = ["a", "b", "c","d", "e", "f", "g", "h"]
play = pygame.image.load("./ChessArt/Buttons/Button_play.png")
log = pygame.image.load("./ChessArt/Buttons/Button_view.png")
help = pygame.image.load("./ChessArt/Buttons/Button_help.png")
currentPlayer = firstBoard.currentPlayer
Moves = ''
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)
red = (200, 0, 0)
purple = (102, 0, 102)
light_gray = ((150,150,150))
midle_gray =((120,120,120))
dark_gray = ((70,70,70))

font = pygame.font.Font(None, 32)
logFileName = ''
logPmoving = ''
PflagEat = False

def createSqParams():
    allSqRanges = []
    xMin = 0
    xMax = 100
    yMin = 0
    yMax = 100
    for _ in range(8):
        for _ in range(8):
            allSqRanges.append([xMin, xMax, yMin, yMax])
            xMin += 100
            xMax += 100
        xMin = 0
        xMax = 100
        yMin += 100
        yMax += 100
    return allSqRanges

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])

def drawChessPieces():
    xpos = 0
    ypos = 25
    color = 0
    width = 100
    height = 100
    black = (66,134,244)
    white = (143,155,175)
    number = 0

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, dark_gray)
                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, white)
                if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load("./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
                xpos += 100

            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 100



def updateChessPieces():

    xpos = 0
    ypos = 25
    number = 0
    newPieces = []

    for _ in range(8):
        for _ in range(8):
            if not firstBoard.gameTiles[number].pieceOnTile.toString() == "-":

                img = pygame.image.load(
                    "./ChessArt/" + firstBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + firstBoard.gameTiles[
                        number].pieceOnTile.toString().upper() + ".png")
                img = pygame.transform.scale(img, (100, 100))

                newPieces.append([img, [xpos, ypos], firstBoard.gameTiles[number].pieceOnTile])
            xpos += 100
            number += 1
        xpos = 0
        ypos += 100

    return newPieces


allSqParams = createSqParams()
drawChessPieces()


def auxWindow(i):
    if i==0:
        fileName = "./BoardFiles/Help/help.txt"
        os.system("start " + fileName)
    else:
        fileName = "./BoardFiles/Log/log.txt"
        os.system("start " + fileName)


def convertion(n):
    columna = n%8
    fila = (n//8)+1
    if columna == 0:
        columna='A'
    elif columna == 1:
        columna = 'B'
    elif columna == 2:
        columna = 'C'
    elif columna == 3:
        columna = 'D'
    elif columna == 4:
        columna = 'E'
    elif columna == 5:
        columna = 'F'
    elif columna == 6:
        columna = 'G'
    elif columna == 7:
        columna = 'H'

    return(columna+str(fila))

def getDataMove(p,fboar,nboar):
    datamove = ''
    if p==0:
        print('Player move')
        datamove=datamove+MovePlayer(fboar,nboar,0)+'-'
        if Eat(fboar,nboar):
            datamove = datamove+'(X):'
        datamove = datamove + MovePlayer(nboar, fboar, 1) + '.'
        ActionsList.append(datamove)
    else:
        print('IA move')
        datamove = datamove + MoveIA(fboar, nboar, 0) + '-'
        if Eat(fboar,nboar):
            datamove = datamove + '(X):'
        datamove = datamove + MoveIA(nboar, fboar, 1) + '.'
        ActionsList.append(datamove)


def MovePlayer(boarx, boary,t):
    for index in range(boarx.getLen()):
        if boarx.isMinus(boarx.getTile(index)):
           if(boarx.getTile(index)!=boary.getTile(index)):
                if t==0:
                    return boarx.getTile(index)+':'+convertion(index)
                else:
                    return convertion(index)



def MoveIA(boarx, boary,t):
    for index in range(boarx.getLen()):
        if boarx.isMayus(boarx.getTile(index)):
           if(boarx.getTile(index)!=boary.getTile(index)):
                if t==0:
                    return boarx.getTile(index)+':'+convertion(index)
                else:
                    return convertion(index)



def Eat(fboar, nboar):
    if (len(fboar.calculateActivePieces(nboar.currentPlayer))-len(nboar.calculateActivePieces(nboar.currentPlayer))!=0):
        return True



def saveLog():
    f= open("./BoardFiles/Log/log.txt","w+")
    for i in range(len(ActionsList)):
        f.write("Move "+str(i+1)+": "+ActionsList[i]+'\n')
    f.close()


selectedImage = None
selectedLegals = None
resetColors = []
quitGame = False
mx, my = pygame.mouse.get_pos()
prevx, prevy = [0,0]



while not quitGame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if selectedImage == None:
                mx, my = pygame.mouse.get_pos()
                for piece in range(len(allPieces)):
                    if allPieces[piece][2].alliance == currentPlayer:

                        if allPieces[piece][1][0] < mx < allPieces[piece][1][0]+100:
                            if allPieces[piece][1][1] < my < allPieces[piece][1][1] + 100:
                                selectedImage = piece
                                prevx = allPieces[piece][1][0]
                                prevy = allPieces[piece][1][1]


                                initialpos = (my // 100 * 8) + mx // 100
                                logPmoving = ''
                                logPmoving = logPmoving+allPieces[selectedImage][2].toString()+':'+convertion(initialpos)+'-'


                                selectedLegals = allPieces[selectedImage][2].calculateLegalMoves(firstBoard)
                                for legals in selectedLegals:
                                    resetColors.append([legals, allTiles[legals][0]])


                                    if allTiles[legals][0] == dark_gray:
                                        allTiles[legals][0] = midle_gray
                                    else:
                                        allTiles[legals][0] = light_gray
                if 825 < mx < 1025:
                    if 275 < my < 353:
                        saveLog()
                        auxWindow(1)
                if 700 < my < 778:
                    if 840 < mx < 1017 and Moves != '':
                        ActionsList.append(Moves)
                        Moves=''
                        #print(ActionsList)
                    if 1000 < mx < 1062:
                        auxWindow(0)



        if event.type == pygame.MOUSEMOTION and not selectedImage == None:

            mx, my = pygame.mouse.get_pos()
            allPieces[selectedImage][1][0] = mx-50
            allPieces[selectedImage][1][1] = my-50


        if event.type == pygame.MOUSEBUTTONUP:

            for resets in resetColors:
                allTiles[resets[0]][0] = resets[1]

            try:
                pieceMoves = allPieces[selectedImage][2].calculateLegalMoves(firstBoard)
                legal = False
                theMove = 0
                for moveDes in pieceMoves:
                    if allSqParams[moveDes][0] < allPieces[selectedImage][1][0]+50 < allSqParams[moveDes][1]:
                        if allSqParams[moveDes][2] < allPieces[selectedImage][1][1]+50 < allSqParams[moveDes][3]:
                            legal = True
                            theMove = moveDes
                if legal == False:
                    allPieces[selectedImage][1][0] = prevx
                    allPieces[selectedImage][1][1] = prevy
                else:
                    allPieces[selectedImage][1][0] = allSqParams[theMove][0]
                    allPieces[selectedImage][1][1] = allSqParams[theMove][2]


                    # TODO make it so it updates board
                    # TODO update moved piece's legal moves some how
                    # print(allPieces[selectedImage][2])
                    # print(firstBoard)
                    thisMove = Move(firstBoard, allPieces[selectedImage][2], theMove)
                    newBoard = thisMove.createNewBoard()
                    getDataMove(0, firstBoard, newBoard)
                    if not newBoard == False:
                        firstBoard = newBoard

                    # else:
                    #     print(newBoard)
                    #firstBoard.printBoard()

                    # TODO update game pieces
                    newP = updateChessPieces()
                    allPieces = newP
                    #print(len(newP))

                    #print(firstBoard.currentPlayer)
                    currentPlayer = newBoard.currentPlayer
                    
                    # TODO add logic that it is AI player
                    if currentPlayer == "Black":
                        aiBoard = True

                        #minimax = Minimax(firstBoard, 1)
                        #aiBoard = minimax.getMove()
                        aiBoard = tree.getBestMove(firstBoard)
                        #aiBoard.printBoard()

                        getDataMove(1,firstBoard,aiBoard)
                        firstBoard = aiBoard

                        # TODO update game pieces
                        newP = updateChessPieces()
                        allPieces = newP
                        currentPlayer = aiBoard.currentPlayer


                    #minimax.board.printBoard()

                    #allPieces[selectedImage][2].position = theMove
                    # allPieces[selectedImage][2].position = theMove
                    # print(allPieces[selectedImage][2].position)

            except:
                pass
                #ActionsList.append('Jaque')


            prevy =0
            prevx = 0
            selectedImage = None

        #print(event)

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(Moves)
                    Moves = ''
                elif event.key == pygame.K_BACKSPACE:
                    Moves = Moves[:-1]
                else:
                    Moves += event.unicode

    gameDisplay.fill((255, 255, 255))
    pygame.draw.rect(gameDisplay, dark_gray, [800, 25, 2, 800])




    #Axix XY
    n = 40
    m = 1
    for x in axis:
        img = pygame.image.load("./ChessArt/xy/"+x+".png")
        img2 = pygame.image.load("./ChessArt/xy/"+str(m)+".png")
        gameDisplay.blit(img, (n, 0))
        gameDisplay.blit(img2, (803, n+25))
        n += 100
        m+=1


    #Buttons
    gameDisplay.blit(play, (840, 700))
    gameDisplay.blit(help, (1000, 700))
    gameDisplay.blit(log, (875, 275))



    #Text
    text = font.render('Input a valid move', True, black)
    textRect = text.get_rect()
    textRect.center=(950,600)
    gameDisplay.blit(text, textRect)


    #Input move
    input_box = pygame.Rect(850, 625, 200, 50)
    txt_surface = font.render(Moves, True, black)
    gameDisplay.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
    pygame.draw.rect(gameDisplay, black, input_box, 2)

    # log of moves
    log_box = pygame.Rect(850, 100, 200, 150)
    if len(ActionsList)>=3:
        txt_log_surface_1 = font.render(ActionsList[-1], True, black)
        txt_log_surface_2 = font.render(ActionsList[-2], True, black)
        txt_log_surface_3 = font.render(ActionsList[-3], True, black)
        gameDisplay.blit(txt_log_surface_3, (log_box.x + 5, log_box.y + 5))
        gameDisplay.blit(txt_log_surface_2, (log_box.x + 5, log_box.y + 45))
        gameDisplay.blit(txt_log_surface_1, (log_box.x + 5, log_box.y + 85))
    elif len(ActionsList)== 2:
        txt_log_surface_1 = font.render(ActionsList[-1], True, black)
        txt_log_surface_2 = font.render(ActionsList[-2], True, black)
        gameDisplay.blit(txt_log_surface_2, (log_box.x + 5, log_box.y + 5))
        gameDisplay.blit(txt_log_surface_1, (log_box.x + 5, log_box.y + 45))
    elif len(ActionsList)== 1:
        txt_log_surface_1 = font.render(ActionsList[-1], True, black)
        gameDisplay.blit(txt_log_surface_1, (log_box.x + 5, log_box.y + 5))
    else:
        txt_log_surface = font.render(' ', True, black)
        gameDisplay.blit(txt_log_surface, (log_box.x + 5, log_box.y + 5))
    pygame.draw.rect(gameDisplay, black, log_box, 2)

    for info in allTiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])



    pygame.display.update()
    clock.tick(60)






