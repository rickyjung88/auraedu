from problem_04 import swap_case


def test_problem_04_case_001():
    assert swap_case("aBcDeF") == "AbCdEf"


def test_problem_04_case_002():
    assert swap_case("ABC") == "abc"


def test_problem_04_case_003():
    assert swap_case("xyz") == "XYZ"


def test_problem_04_case_004():
    assert swap_case("Hello World!") == "hELLO wORLD!"


def test_problem_04_case_005():
    assert swap_case("123abcDEF") == "123ABCdef"
