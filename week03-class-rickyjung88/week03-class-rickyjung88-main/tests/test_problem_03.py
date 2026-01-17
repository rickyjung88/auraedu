from problem_03 import my_round


def test_problem_03_case_001():
    assert my_round(5, 0) == 10


def test_problem_03_case_002():
    assert my_round(14, 0) == 10


def test_problem_03_case_003():
    assert my_round(15, 0) == 20


def test_problem_03_case_004():
    assert my_round(1234, 1) == 1200


def test_problem_03_case_005():
    assert my_round(1250, 1) == 1300


def test_problem_03_case_006():
    assert my_round(2.499, -1) == 2


def test_problem_03_case_007():
    assert my_round(2.5, -1) == 3


def test_problem_03_case_008():
    assert my_round(2.449, -2) == 2.4


def test_problem_03_case_009():
    assert my_round(2.451, -2) == 2.5
