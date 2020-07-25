class NeuralNet():
    """
    사용자 정의 Neural Network 정의
    플레이어가 누군지는 상관하지 않고 오직
    canonical 한 형태로만 게임판을 인식함
    """
    def __init__(self, game):
        pass
    
    def train(self, examples):
        """
        self-play에서 neural network를 훈련시킴
        Input:
            example: 트레이닝 예제의 리스트
            (board, pi, v)의 형태
            pi는 MCTS의 pi의 정책
            v는 value
        """
        pass

    def predict(self, board):
        """
        Input:
            board: canonical한 형태의 게임판

        Returns:
            pi: game.getActionSize 길이의 정책 벡터
            v: [-1, 1]로 나타내지는 현 게임판의 가치
        """
        pass
    
    def save_checkpoint(self, folder, filename):
        """
        neural network의 파라미터를 folder/filename에 저장
        """
        pass
    
    def load_checkpoint(self, folder, filename):
        """
        파라미터 불러오기
        """
        pass
