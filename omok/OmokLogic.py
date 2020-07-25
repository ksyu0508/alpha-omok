#-*- coding:utf-8 -*-

class Board():
    
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
    def __init__(self, n=15):
        #�????�성
        self.n = n
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [0]*self.n
        self.directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
    
    def __getitem__(self, index):
        return self.pieces[index]
        
    def nearby(self, x, y):
        
        if x < 7 and x > 3 and y < 7 and y > 3:
            cnt = 0
            for i in range(4, 7):
                for j in range(4, 7):
                    if self[i][j] ==0:
                        cnt += 1
            if cnt == 9:
                return True
        
        for i, j in self.directions:
            if x+i >= 0 and x+i < self.n and y+j >= 0 and y+j < self.n:
                if self[x+i][y+j] != 0:
                    return True
        return False
        
    def find_sam(self, x, y, color):
        
        for i, j in self.directions:
            if x+3*i >= 0 and x+3*i < self.n and y+3*j >= 0 and y+3*j < self.n:
                if self[x+i][y+j] == -color and self[x+2*i][y+2*j] == -color and self[x+3*i][y+3*j] == -color:
                    return True
        return False
    
    def get_legal_moves(self, color):
        

        moves = set()

        ##?�행 가?�한 �?리턴, ?�기?�는 �?�?리턴
        
        if color == -1:
          for y in range(self.n):
              for x in range(self.n):
                  if self[x][y]==0:
                      newmove = (x,y)
                      moves.add(newmove)
        elif color == 1:
            if self.is_sam(-color):
                for y in range(self.n):
                    for x in range(self.n):
                        if self[x][y]==0 and self.find_sam(x, y, color):
                            newmove = (x,y)
                            moves.add(newmove)
                            
            if(len(list(moves))!=0):
                return list(moves)

            for y in range(self.n):
                for x in range(self.n):
                    if self[x][y]==0 and self.nearby(x, y):
                        newmove = (x,y)
                        moves.add(newmove)
              
        return list(moves)

    def has_legal_moves(self):
        #"""
        #가?�한 ?�직임???�는지 ?�는지 리턴?�듯
        #get_legal_moves�??��?가?�할??
        #"""
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y] == 0:

                    return True

        return False
    
    def is_win(self, color):
        #"""
        #백�? 1, ?��? -1
        #?��? ?�겼?��? 체크, 리턴
        #"""
        win = 5
        # x방향 체크
        for y in range(self.n):
            count = 0
            for x in  range(self.n):
                if self[x][y]==color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        # y방향 체크
        for x in range(self.n):
            count = 0
            for y in range(self.n):
                if self[x][y]==color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        # / 방향 체크
        for x in range(self.n):
            count = 0
            for i in range(self.n - x):
                if self[x+i][i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        for y in range(self.n):
            count = 0
            for i in range(self.n-y):
                if self[i][y+i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        # \ 방향 체크
        for x in range(self.n):
            count = 0
            for i in range(x+1):
                if self[i][x-i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
            
        for y in range(self.n):
            count = 0
            for i in range(self.n-y):
                if self[self.n-1-i][y+i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True

        return False
    
    def is_sam(self, color):
        #"""
        #백�? 1, ?��? -1
        #?��? ?�겼?��? 체크, 리턴
        #"""
        win = 3
        # x방향 체크
        for y in range(self.n):
            count = 0
            for x in  range(self.n):
                if self[x][y]==color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        # y방향 체크
        for x in range(self.n):
            count = 0
            for y in range(self.n):
                if self[x][y]==color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        # / 방향 체크
        for x in range(self.n):
            count = 0
            for i in range(self.n - x):
                if self[x+i][i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        for y in range(self.n):
            count = 0
            for i in range(self.n-y):
                if self[i][y+i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
        # \ 방향 체크
        for x in range(self.n):
            count = 0
            for i in range(x+1):
                if self[i][x-i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True
            
        for y in range(self.n):
            count = 0
            for i in range(self.n-y):
                if self[self.n-1-i][y+i] == color:
                    count += 1
                else:
                    count = 0
                if count == win:
                    return True

        return False
    
    def execute_move(self, move, color):
        #"""
        #주어�??�직임???�?�서 게임?�에 ?�을 ?�는??
        #�? move???�치???�자�?color�?바꿈
        #"""

        (x, y) = move
        # assert self[x][y] == 0
        self[x][y] = color
