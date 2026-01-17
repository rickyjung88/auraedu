from problem_02 import alphabet_first_positions


def test_problem_02_case_001():
    assert alphabet_first_positions("baekjoon") == [
        1,
        0,
        -1,
        -1,
        2,
        -1,
        -1,
        -1,
        -1,
        4,
        3,
        -1,
        -1,
        7,
        5,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ]


def test_problem_02_case_002():
    assert alphabet_first_positions("abcdefghijklmnopqrstuvwxyz") == list(range(26))


def test_problem_02_case_003():
    assert alphabet_first_positions("aaaaa") == [0] + [-1] * 25


def test_problem_02_case_004():
    assert alphabet_first_positions("z") == [-1] * 25 + [0]


def test_problem_02_case_005():
    assert alphabet_first_positions("abcabc") == [0, 1, 2] + [-1] * 23
