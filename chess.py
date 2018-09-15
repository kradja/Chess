import pdb
import numpy as np
import pandas as pd
from string import Template

class board_pieces():
    def __init__(self):
        self.board = np.zeros(shape=(8,8)) #Regular size of chess board
        # SHOULD USE TEMPLATES
        self.zsize = self.board.shape[0] - 1
        self.pieces = {'pawn':[1,[1,list(range(0,self.board.shape[0]))]],'knight':[2,[0,[1,self.zsize-1]]],
                       'bishop':[3,[0,[2,self.zsize-2]]],'castle':[4,[0,[0,self.zsize]]],'queen':[5,[0,[3]]],
                       'king':[6,[0,[4]]]}
    def getpiece(self,piece):
        return self.pieces[piece][0]
    def locpiece(self,piece):
        return self.pieces[piece][1]
    def setpieces(self):
        for piece in self.pieces.keys():
            row,col = self.locpiece(piece)
            self.board[row][col] = self.getpiece(piece)
        self.board[[self.zsize,self.zsize-1]] = -self.board[[0,1]]
        pdb.set_trace()
    def pawnrules(self):
        print('pawn') 
def main():
    bp = board_pieces()
    bp.setpieces()
if __name__ == '__main__':
    main()
