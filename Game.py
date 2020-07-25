class Game():
    """
    사용자 정의 게임을 위해서는 이 클래스를 상속
    턴 기반, 적대적인 2명의 플레이어에서만 작동함
    """

    def __init__(self):
        pass

    def getInitBoard(self):
        """
        startBoard를 리턴(representaion of board)
        뉴럴 넷에 들어갈 형태 만들자
        """
        pass

    def getBoardSize(self):
        """
        게임판의 크기를 tuple로 리턴
        (x, y)
        """
        pass
    
    def getActionSize(self):
        """
        가능한 모든 행동의 수 리턴
        """
        pass
    
    def getNextState(self, board, player, action):
        """
        Input:
            board: 현재 게임판
            player: 현재 플레이어 (1 or -1)
            action: 현재 플레이어가 취한 행동

        Returns:
            nextBoard: 행동을 취한 후 다음 게임판
            nextPlayer: 다음 턴에 플레이 할 사람 (-를 취하자)
        """
        pass

    def getValidMoves(self, board, player):
        """
        Input:
            board: 현재 게임판
            player: 현재 플레이어

        Returns:
            validMoves: getActionSize로 받은 차원의 binary vector
            1이면 가능한 움직임, 0이면 불가능한 움직임
        """
        pass

    def getGameEnded(self, board, player):
        """
        Input:
            board:
            player:

        Returns:
            r:  0이면 끝나지 않은 상태
                1이면 player 1 승리
                -1이면 패배
                셋다 아니면 비김
        """
        pass
    
    def getCanonicalForm(self, board, player):
        """
        Input:
            board
            player
        
        Returns:
            canonicalBoard: 정규 게임판?
                게임판의 정규적인 형태를 리턴
                정규 형태는 플레이어에게 독립적임
                예를 들어 체스의 경우
                백의 시점에서 정규 형태가 골라질 수 있어야한다
                플레이어가 백이면 우리는 백의 보드를 리턴해야하고
                흑이면 색을 반전시켜서 리턴해야한다. ??
        """
        pass

    def getSymmetries(self, board, pi):
        """
        Input:
            board
            pi: policy getActionSize 크기의 policy 벡터

        Returns:
            symmForms: [(board, pi)]의 리스트
                        각각의 쌍은  대칭적은 게임판의 형태와 이에 따른 정책 벡터
                        neural net에 예시로서 학습할 때에 사용
        """
        pass

    def stringRepresentation(self, board):
        """
        Input:
            board
        
        Returns:
            boardString: string 형태의 간단한 게임판 전환
                        MCTS를 hashing 할 때에 필요
        """
        pass