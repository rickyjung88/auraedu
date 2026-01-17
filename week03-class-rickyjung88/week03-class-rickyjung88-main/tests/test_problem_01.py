from problem_01 import nth_prime


def test_problem_01_case_001():
    assert nth_prime(1) == 2


def test_problem_01_case_002():
    assert nth_prime(2) == 3


def test_problem_01_case_003():
    assert nth_prime(3) == 5


def test_problem_01_case_004():
    assert nth_prime(5) == 11


def test_problem_01_case_005():
    assert nth_prime(6) == 13


def test_problem_01_case_006():
    assert nth_prime(10) == 29


def test_problem_01_case_007():
    assert nth_prime(100) == 541


def test_problem_01_case_008():
    assert nth_prime(1000) == 7919


def test_problem_01_case_009():
    assert nth_prime(10000) == 104729
