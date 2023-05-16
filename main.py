from dataclasses import dataclass
from enum import Enum
from os import system
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
        if x == self.width - 1 and y == self.length - 1:
            return True
        else:
            return False

    
    def print_board(self):
        board = ""  
        for y in range(self.length):
            for x in range (self.width):
                if self.turtle_location == (x,y):
                    board = board + "T"
                else:
                    if self.is_goal(x,y) == False:
                        board = board + "."
                    else:
                        board = board + "G"
            if y < self.length-1:
                board = board + "\n"
        return(board)
                
        """Prints the board with the turtle's location marked with a T and the goal location marked with a G."""
        
    
    def move_turtle(self):
        """Updates the turtle's location"""
        (x,y) = self.turtle_location
        if self.turtle.orientation == Direction.EAST:
            newx = min(x+self.turtle.speed,self.width-1)
            (x,y)= (newx,y)
                
        if self.turtle.orientation == Direction.NORTH:
            newy = max(y-self.turtle.speed,0)
            (x,y)= (x,newy)
            
        if self.turtle.orientation == Direction.WEST:
            newx = max(x-self.turtle.speed,0)
            (x,y)= (newx,y)
        
        if self.turtle.orientation == Direction.SOUTH:
            newy = min(y+self.turtle.speed,self.length-1)
            (x,y)= (x,newy)
        self.turtle_location = (x,y)
        print(x,y)
        
            
    def change_orientation(self, rotate_right=True):
        # False means rotate left
        # For example: if the turtle's previous orientation was NORTH and rotate_right is True, the new orientation should be EAST
        if self.turtle.orientation == Direction.NORTH:
            if rotate_right == True:
                self.turtle.orientation = Direction.EAST
            else:
                self.turtle.orientation = Direction.WEST
                
        elif self.turtle.orientation == Direction.EAST:
            if rotate_right == True:
                self.turtle.orientation = Direction.SOUTH
            else:
                self.turtle.orientation = Direction.NORTH
                
        elif self.turtle.orientation == Direction.SOUTH:
            if rotate_right == True:
                self.turtle.orientation = Direction.WEST
            else:
                self.turtle.orientation = Direction.EAST
                
        elif self.turtle.orientation == Direction.WEST:
            if rotate_right == True:
                self.turtle.orientation = Direction.NORTH
            else:
                self.turtle.orientation = Direction.SOUTH



    def turtle_is_at_goal(self):
        (x,y) = self.turtle_location
        return self.is_goal(x,y)
