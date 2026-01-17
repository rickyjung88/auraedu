from problem_06 import does_word_exist_in_board


def test_problem_03_case_001():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCB"
    assert does_word_exist_in_board(board, word) is False


def test_problem_03_case_002():
    board = [["A"]]
    word = "AAAAA"
    assert does_word_exist_in_board(board, word) is False


def test_problem_03_case_003():
    board = [["A"]]
    word = "B"
    assert does_word_exist_in_board(board, word) is False


def test_problem_03_case_004():
    board = [["A", "B", "C", "D", "E"]]
    word = "ABCDE"
    assert does_word_exist_in_board(board, word) is True


def test_problem_03_case_005():
    board = [
        ["A", "B", "C"],
        ["H", "G", "D"],
        ["I", "F", "E"],
    ]
    word = "ABCDEFGHI"
    assert does_word_exist_in_board(board, word) is True


def test_problem_03_case_006():
    board = [
        ["A", "B"],
        ["C", "A"],
    ]
    word = "ABACA"
    assert does_word_exist_in_board(board, word) is False


def test_problem_03_case_007():
    board = [
        ["B", "B"],
        ["B", "B"],
    ]
    word = "A"
    assert does_word_exist_in_board(board, word) is False


def test_problem_03_case_008():
    board = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"],
    ]
    word = "ABCFI"
    assert does_word_exist_in_board(board, word) is True


def test_problem_03_case_009():
    board = [
        ["A", "A"],
        ["A", "A"],
    ]
    word = "AAAAAAAAAA"
    assert does_word_exist_in_board(board, word) is False


def test_problem_03_case_010():
    board = [
        ["A", "B"],
        ["C", "D"],
    ]
    word = ""
    assert does_word_exist_in_board(board, word) is True
