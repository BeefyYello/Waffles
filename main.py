from dataclasses import dataclass
from enum import Enum
from typing import Tuple

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


@dataclass
class Turtle:
    speed: int
    orientation: Direction


@dataclass
class GameBoard:
    """This represents a rectangular grid. Smaller values of <length> represent locations nearer the top.
    Smaller values of <width> represent locations nearer the left side.
    The goal is for the turtle to reach the bottom right corner of the grid.
    This is zero-indexed: the top-left corner is (0, 0), not (1, 1)
    """

    length: int
    width: int
    turtle: Turtle = Turtle(1, Direction.EAST)
    turtle_location: Tuple[int, int] = (0, 0)

    def is_goal(self, x: int, y: int) -> bool:
        if x == self.width - 1 and y == self.width - 1:
            return True
        else:
            return False
        
    
    def move_turtle(self):
        """Updates the turtle's location"""
        raise NotImplementedError

