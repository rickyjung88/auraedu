from typing import Union


def my_round(a: float, k: int) -> Union[int, float]:
    """
    숫자를 10**k 자릿수에서 반올림합니다 (일의 자리가 0번째).
    k번째 자리 숫자가 5 이상이면 올림하고, 그렇지 않으면 내림합니다.

    Args:
        a (float): 반올림할 양수 (음수는 허용되지 않음)
        k (int): 반올림할 자릿수 (0은 일의 자리, 1은 십의 자리, -1은 소수점 첫째 자리)

    Returns:
        Union[int, float]: 반올림된 결과 (정수인 경우 int, 소수인 경우 float)

    Examples:
        my_round(123.456, 0) -> 123 (일의 자리에서 반올림)
        my_round(123.456, 1) -> 120 (십의 자리에서 반올림)
        my_round(123.456, -1) -> 123.5 (소수점 첫째 자리에서 반올림)
    """
    raise NotImplementedError
