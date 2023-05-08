from dataclasses import dataclass


@dataclass
class GameBoard:
    """This represents a rectangular grid. Smaller values of <length> represent locations nearer the top.
    Smaller values of <width> represent locations nearer the left side.
    The goal is for the turtle to reach the bottom right corner of the grid.
    This is zero-indexed: the top-left corner is (0, 0), not (1, 1)
    """

    length: int
    width: int

    def is_goal(self, x: int, y: int) -> bool:
        """Returns True if and only if the coordinates (x, y) represent the bottom right corner of the grid."""
        raise NotImplementedError


def victory_message():
    return "You made it to the goal!"
