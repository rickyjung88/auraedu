from typing import List


def does_word_exist_in_board(board: List[List[str]], word: str) -> bool:
    """
    각 원소가 알파벳 하나로 이루어진 이차원 리스트(보드)가 주어졌을 때,
    인접한 원소들을 이어서 주어진 단어를 만들 수 있는지 확인하는 함수입니다.

    Args:
        board (List[List[str]]): 알파벳으로 구성된 2차원 보드
        word (str): 찾을 단어

    Returns:
        bool: 단어를 만들 수 있으면 True, 없으면 False

    Note:
        - 인접한 원소는 상하좌우로 연결된 원소를 의미합니다
        - 이미 사용한 원소는 다시 사용할 수 없습니다 (problem_05와의 차이점)
        - 대각선으로는 연결되지 않습니다

    Examples:
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

        보드 시각화:
        A B C E
        S F C S
        A D E E

        does_word_exist_in_board(board, "ABCB") # False (B를 두 번 사용해야 하므로)
        does_word_exist_in_board(board, "ABCCED") # True
        가능한 경로: A(0,0) -> B(0,1) -> C(0,2) -> C(1,2) -> E(0,3) -> D(2,1)
    """
    raise NotImplementedError
