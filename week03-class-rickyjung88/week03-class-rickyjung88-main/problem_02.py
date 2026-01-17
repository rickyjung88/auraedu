from typing import List


def alphabet_first_positions(s: str) -> List[int]:
    """
    문자열에서 각 소문자 알파벳 a-z가 처음으로 나타나는 인덱스를 반환합니다.
    문자열에 없는 문자는 -1로 표시됩니다.

    Args:
        s (str): 검사할 문자열

    Returns:
        List[int]: 각 알파벳 a-z의 첫 번째 위치를 담은 리스트 (길이 26)
                   예: 'hello' -> a부터 z까지 순서대로 [-1, -1, -1, -1, 1, -1, ..., -1, -1, -1]
    """
    raise NotImplementedError
