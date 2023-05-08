from main import GameBoard


def test_game_board_can_be_created():
    # This mostly exists to make sure that errors don't happen on initialization.
    assert GameBoard(length=1, width=1)


def test_is_goal_returns_true_for_bottom_right_corner():
    board = GameBoard(length=10, width=10)
    assert board.is_goal(x=9, y=9)


def test_is_goal_returns_false_for_other_corner():
    board = GameBoard(length=10, width=10)
    assert not board.is_goal(x=0, y=9)


def test_is_goal_returns_false_with_one_indexing():
    # One mistake we anticipate is for users of GameBoard to expect the board
    # to be indexed from 1 instead of 0. Make sure GameBoard doesn't do this.
    board = GameBoard(length=10, width=10)
    assert not board.is_goal(x=10, y=10)
