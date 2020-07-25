# alpha-omok

[발표자료]<https://github.com/ksyu0508/alpha-omok/blob/master/2019-2_%EC%BB%A8%ED%8D%BC%EB%9F%B0%EC%8A%A4_%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf>

| |알파제로|알파고|
|---|---|---|
|상대전적|100승|100패|
|초기 데이터|X|16만개의 기보|
|학습방법|자가대국|사전데이터 학습 후 자가대국|
|신경망|통합됨|가치망, 정책망|
|학습시간|3일(4TPU)|40일(48TPU)|

## 학습 환경
GCP 인스턴스
- CPU: 6 core
- RAM: 24GB
- GPU: Tesla V100

## 실행 예시
![example](./imgs/강화.gif)

![endgame](./imgs/endgame.png)

좋은 성능을 나타내지는 않지만 random player보다는 우세한 성능을 보여주고 위 그림처럼 오목을 찾아내는 모습을 보여준다. 이를 통해서 학습은 진행되고 있었음을 알 수 있다.

약 2일 정도 학습시켰으며, gcp 크레딧과 느린 수렴 속도의 문제로 도중에 중단할 할 수 밖에 없었다.
리소스의 한계도 있고 어려운 학습 조건도 문제였다.
다른 성공한 예시들의 경우에는 대부분 tic-tac-toe나 오셀로 아니면 8x8정도 사이즈의 오목이다.
게임판의 크기를 줄여주거나, 사목정도로 승리 조건의 난이도를 낮춘다면 더 빠른 학습이 가능할 것이다.

## Thanks to
- YBIGTA 15기 김정학
- YBIGTA 15기 송하룡
- YBIGTA 15기 조준흠
- YBIGTA 15기 최종문

## 참고자료
- [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815)
- <https://github.com/suragnair/alpha-zero-general>
