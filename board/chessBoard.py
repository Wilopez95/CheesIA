from board.tile import Tile
from pieces.nullPiece import NullPiece
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook


class Board:

    gameTiles = {}
    enPassPawn = None
    enPassPawnBehind = None
    currentPlayer = ""

    def __init__(self):
        pass

    def calculateActivePieces(self, alliance):

        activeP = []
        for tile in range(len(self.gameTiles)):
            if not self.gameTiles[tile].pieceOnTile.toString() == "-":
                if self.gameTiles[tile].pieceOnTile.alliance == alliance:
                    activeP.append(self.gameTiles[tile].pieceOnTile)

        return activeP

    def calculateLegalMoves(self, pieces, board):
        allLegals = []
        for piece in pieces:
            pieceMoves = piece.calculateLegalMoves(board)
            for move in pieceMoves:
                allLegals.append([move, piece])
        return allLegals


    def createBoard(self,filename):
        file1 = open('BoardFiles/'+filename+'.cfl', 'r')
        count = -1
        while True:
            line = file1.readline()
            if not line:
                break
            if line[0] != '#':
                if line != '\n':
                    if line[0] == 'W' or line[0] == 'B' :
                        pass
                        self.currentPlayer = line[0:5]
                    else:
                        for x in range(2,18):
                            if(line[x] != '|'):
                                count += 1
                                #print(count,line[x])
                                self.loadPieces(count,line[x])

        file1.close()

    def loadPieces(self,n,p):
        if(p=='K'):
            self.gameTiles[n] = Tile(n, King("Black", n))
        elif(p=='k'):
            self.gameTiles[n] = Tile(n, King("White", n))
        elif(p=='Q'):
            self.gameTiles[n] = Tile(n, Queen("Black", n))
        elif(p=='q'):
            self.gameTiles[n] = Tile(n, Queen("White", n))
        elif(p=='N'):
            self.gameTiles[n] = Tile(n, Knight("Black", n))
        elif(p=='n'):
            self.gameTiles[n] = Tile(n, Knight("White", n))
        elif(p=='B'):
            self.gameTiles[n] = Tile(n, Bishop("Black", n))
        elif(p=='b'):
            self.gameTiles[n] = Tile(n, Bishop("White", n))
        elif(p=='R'):
            self.gameTiles[n] = Tile(n, Rook("Black", n))
        elif(p=='r'):
            self.gameTiles[n] = Tile(n, Rook("White", n))
        elif(p=='P'):
            self.gameTiles[n] = Tile(n, Pawn("Black", n))
        elif(p=='p'):
            self.gameTiles[n] = Tile(n, Pawn("White", n))
        else:
            self.gameTiles[n] = Tile(n,NullPiece())


    def printBoard(self):
        count = 0
        for tiles in range(len(self.gameTiles)):
            print('|', end=self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0

    def getLen(self):
        return len(self.gameTiles)

    def getTile(self,i):
        return self.gameTiles[i].pieceOnTile.toString()

    def isMinus(self,x):
        if x=='k':
            return True
        elif x=='q':
            return True
        elif x=='n':
            return True
        elif x=='b':
            return True
        elif x=='r':
            return True
        elif x=='p':
            return True
        else:
            return False

    def isMayus(self,x):
        if x=='K':
            return True
        elif x=='Q':
            return True
        elif x=='N':
            return True
        elif x=='B':
            return True
        elif x=='R':
            return True
        elif x=='P':
            return True
        else:
            return False