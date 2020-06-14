from board import chessBoard
from board.move import Move
from player.boardEvaluator import BoardEvaluator


# firstBoard = chessBoard.Board()
# firstBoard.createBoard()

# TODO
# Poda
#

class DesicionTree:
    bestMove = None
    boardEvaluator = None
    # alpha value for prunning
    maxScore = 0
    # beta value for prunning
    minScore = 0
    maxLevel = 5
    player = None

    def __init__(self, maxLevel):
        self.maxLevel = maxLevel
        self.boardEvaluator = BoardEvaluator()
        self.reset()

    def reset(self):
        self.bestMove = None
        self.maxScore = 0
        self.minScore = 0

    # always return a board object
    def getBestMove(self, board):
        print("getting next move")
        self.player = board.currentPlayer
        print(self.player)
        bestboard = self.getNextMove(board, -1000000000, 100000000, 0).board
        print("got next move")
        return bestboard

    # always returns a node object
    def getNextMove(self, board, alpha, beta, level):
        # return if depth reached
        if (level >= self.maxLevel):
            boardValue = self.boardEvaluator.evaluate(self.player, board, level)
            return Node(board, boardValue)

        # explore childe nodes
        currentPlayer = board.currentPlayer
        # get all posible moves
        allPieces = board.calculateActivePieces(currentPlayer)
        allLegalMoves = board.calculateLegalMoves(allPieces, board)

        selectedNode = None
        maxEva = -100000000
        minEva = 100000000
        for move in allLegalMoves:
            newMove = Move(board, move[1], move[0])
            newboard = newMove.createNewBoard()
            # extra check for move validity
            if not isinstance(newboard, bool):
                minmaxNode = self.getNextMove(newboard, alpha, beta, level + 1)
                if (minmaxNode == None):
                    continue
                newNode = Node(newboard, minmaxNode.value)
                if (self.isMax(level)):
                    selectedNode = self.getMaxNode(selectedNode, newNode)
                    maxEva = max(maxEva, selectedNode.value)
                    alpha = max(alpha, maxEva)
                    if (beta <= alpha):
                        # print("prunned")
                        break
                else:
                    selectedNode = self.getMinNode(selectedNode, newNode)
                    minEva = min(minEva, selectedNode.value)
                    beta = min(beta, minEva)
                    if (beta <= alpha):
                        # print("prunned")
                        break

        return selectedNode

    def isMax(self, level):
        return level % 2 == 0

    def getMinNode(self, nodeA, nodeB):
        if (nodeA == None):
            return nodeB
        if (nodeA == None):
            return nodeA
        if (nodeA.value > nodeB.value):
            return nodeB
        else:
            return nodeA

    def getMaxNode(self, nodeA, nodeB):
        if (nodeA == None):
            return nodeB
        if (nodeA == None):
            return nodeA
        if (nodeA.value < nodeB.value):
            return nodeB
        else:
            return nodeA


class Node:
    board = None
    value = None

    def __init__(self, board, value):
        self.board = board
        self.value = value

    def printself(self):
        print(self.board.currentPlayer + " " + str(self.value))

# tree = DesicionTree(3)
# print(tree.getBestMove(firstBoard))