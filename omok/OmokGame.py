from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .OmokLogic import Board
import numpy as np

class OmokGame(Game):
    def __init__(self, n=15):
        self.n = n

    def getInitBoard(self):
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        return (self.n, self.n)
    
    def getActionSize(self):
        return self.n*self.n+1
    
    def getNextState(self, board, player, action):
        if action == self.n*self.n:
            return (board, -player)

        b = Board(self.n)
        b.pieces = np.copy(board)
        move = (int(action/self.n), action%self.n)
        b.execute_move(move, player)

        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves = b.get_legal_moves(player)
        if len(legalMoves) == 0:
            # valids[-1] = 1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.n*x+y] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):

        b = Board(self.n)
        b.pieces = np.copy(board)

        if b.is_win(player):
            return 1
        if b.is_win(-player):
            return -1
        if b.has_legal_moves():
            return 0
        
        return 1e-4
    
    def getCanonicalForm(self, board, player):
        return player*board

    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert(len(pi) == self.n**2+1)
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        return board.tostring()
    
    @staticmethod
    def display(board):
        n = board.shape[0]

        print("    ", end="")

        for y in range(n):
            print(format(y, "<2"),end="")
        print("")
        for y in range(n):
            print(format(y, "2"), "|", end="")
            for x in range(n):
                piece = board[y][x]
                if piece == -1: print("X ", end="")
                elif piece == 1 : print("O ", end="")
                else:
                    if x==n:
                        print("-", end="")
                    else:
                        print("- ", end="")
            print("|")
        print("   ", end='')
        for _ in range(n):
            print("-", end="-")
        print("--")