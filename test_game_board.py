from main import Direction, GameBoard, Turtle


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


def test_turtle_moving_basic_case():
    board = GameBoard(10, 10, Turtle(1, Direction.EAST))
    board.move_turtle()
    assert board.turtle_location == (1, 0)

def test_turtle_moving_basic_case_north_south():
    board = GameBoard(10, 10, Turtle(1, Direction.SOUTH))
    board.move_turtle()
    assert board.turtle_location == (0, 1)

def test_turtle_moving_higher_speed():
    board = GameBoard(10, 10, Turtle(3, Direction.EAST))
    board.move_turtle()
    assert board.turtle_location == (3, 0)


def test_turtle_does_not_go_off_board_east_west():
    board = GameBoard(10, 10, Turtle(3, Direction.EAST), (8, 0))
    board.move_turtle()
    assert board.turtle_location == (9, 0)

def test_turtle_does_not_go_off_board_north_south():
    board = GameBoard(10, 10, Turtle(4, Direction.NORTH), (5, 2))
    board.move_turtle()
    assert board.turtle_location == (5, 0)

def test_game_board_printing_3_by_3_basic_case():
    board = GameBoard(3, 3, Turtle(1, Direction.EAST), (0, 0))
    assert board.print_board() == "T..\n...\n..G"

def test_game_board_printing_3_by_3_after_move():
    board = GameBoard(3, 3, Turtle(2, Direction.EAST), (0, 1))
    assert board.print_board() == "...\nT..\n..G"

def test_game_board_printing_5_by_3_after_move():
    board = GameBoard(5, 3, Turtle(2, Direction.EAST), (0, 1))
    assert board.print_board() == "...\nT..\n...\n...\n..G"

def test_turtle_is_at_goal_false():
    board = GameBoard(10, 10, Turtle(1,Direction.EAST),(0,0))
    assert board.turtle_is_at_goal() == False
    
def test_turtle_is_at_goal_true():
    board = GameBoard(1,1, Turtle(1, Direction.EAST),(0,0))
    assert board.turtle_is_at_goal() == True
    

def test_north_turn_right():
    board = GameBoard(3, 3, Turtle(2, Direction.EAST), (0,0))
    board.move_turtle()
    board.change_orientation()
    board.move_turtle()
    assert board.turtle_is_at_goal() == True

def test_north_turn_left():
    board = GameBoard(3,3, Turtle(2, Direction.SOUTH), (0,0))
    board.move_turtle()
    board.change_orientation(False)
    board.move_turtle()
    assert board.turtle_is_at_goal() == True

def test_distance_to_goal_basic_case():
    board = GameBoard(3, 3)
    assert board.distance_to_goal() == 4

def test_distance_to_goal_other_case():
    # The distance is the same even if the orientation is different
    board = GameBoard(25, 42, Turtle(2, Direction.NORTH), (3, 3))
    # I'm pretty sure this arithmetic is right, but please excuse me (and please correct it) if it's wrong.
    assert board.distance_to_goal() == 59
