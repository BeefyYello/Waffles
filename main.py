from dataclasses import dataclass
import math
from enum import Enum
from os import system
from typing import List, Tuple
import random

from dataclasses import dataclass, field
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
    barrier_list:List = field(default_factory= list) #My dad told me to do this instead of None

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
                elif (x,y) in self.barrier_list:
                    board = board + "X"
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
        for i in range(self.turtle.speed): 
            if self.turtle.orientation == Direction.EAST:
                newx = min(x+1,self.width-1)
                (x,y)= (newx,y)
                    
            if self.turtle.orientation == Direction.NORTH:
                newy = max(y-1,0)
                (x,y)= (x,newy)
            
            if self.turtle.orientation == Direction.WEST:
                newx = max(x-1,0)
                (x,y)= (newx,y)
        
            if self.turtle.orientation == Direction.SOUTH:
                newy = min(y+1,self.length-1)
                (x,y)= (x,newy)
                
            if (x,y) in self.barrier_list:
                return False
        self.turtle_location = (x,y)
                
        return True
            
                
        

       

    def change_speed(self, turtlespeed: int):
        self.turtle.speed = turtlespeed
        return
        
            
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

    def distance_to_goal(self):
        """Return the length of a shortest path from the turtle to the goal."""
        (x,y) = self.turtle_location
        (a,b) = (self.width - 1, self.length - 1)
        return abs((x - a) + (y - b))

    def moves_to_goal(self):
        (x,y) = self.turtle_location
        (a,b) = (self.width - 1, self.length - 1)
        return abs(math.ceil((a-x)/self.turtle.speed) + math.ceil((b-y)/self.turtle.speed))

    def turtle_is_at_goal(self):
        (x,y) = self.turtle_location
        return self.is_goal(x,y)
    
    def add_random_barrier(self):
        barriercoordx = random.randint(0,self.width -1)
        if barriercoordx == 0:
            barriercoordy = random.randint(1,self.length-1)

        else:
            barriercoordy = random.randint(1,self.length -1)
        self.append_barrier_list(barriercoordx, barriercoordy)

            
    def append_barrier_list(self, barriercoordx, barriercoordy):        
        self.barrier_list.append((barriercoordx,barriercoordy))
        
            


if __name__=="__main__":
    board = GameBoard(5, 5)
    board.add_random_barrier()



    while True:
        system("clear")
        print(board.print_board())
        print("\nHi, and welcome to my game! \n To move forward, press any button then enter except for r, press to turn right, l, press to turn left, and any integer to change the speed of the turtle.")
        next_input = input()
        if next_input in ("q", "Q"):
            break
    
            
        elif next_input in ("l", "L"):
            board.change_orientation(False)
        elif next_input in ("r", "R"):
            board.change_orientation(True)
        elif next_input.isdigit():
            
            board.change_speed(int(next_input))
       
            
        else:
            result = board.move_turtle()
            if result == False:
                print("YOU MESSED UP! BU BYE")
                break
            if board.turtle_is_at_goal()== True:
                print("Congratulations! You won!")
                quit()
        
        
