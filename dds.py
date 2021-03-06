#!/usr/bin/env python3

from time import time
from random import choice
from board import Board
from element import Element
from direction import Direction

class DirectionSolver:
    """ This class should contain the movement generation algorythm."""
    
    def __init__(self):
        self._direction = None
        self._board = None
        self._last = None
        self._count = 0

    def get(self, board_string):
        """ The function that should be implemented."""
        self._board = Board(board_string)
        _command = self.find_direction()
        print("Sending Command {}".format(_command))
        return _command

    def find_direction(self):
        """ This is an example of direction solver subroutine."""
        _direction = Direction('NULL').to_string()
        if self._board.is_my_bomberman_dead():
            print("Bomberman is dead. Sending 'NULL' command...")
            return _direction
        # here's how we find the current Point of our bomberman
        _bm = self._board.get_bomberman()
        _bm_x, _bm_y = _bm.get_x(), _bm.get_y()
        # Let's check whether our bomberman is not surrounded by walls
        if 4 == self._board.count_near(_bm_x, _bm_y, Element('DESTROY_WALL')):
            print("It seems like walls surround you. Self-destroying.")
            return Direction('ACT').to_string()  # Let's drop a bomb then
        #print(self._board.to_string())
        print("Found your Bomberman at {}".format(_bm))
        # here's how we get the list of barriers Points
        _barriers = self._board.get_barriers()
        _deadline = time() + 30
        while time() < _deadline:
            # here we get the random direction choise
            __dir = Direction(choice(('LEFT', 'RIGHT', 'DOWN', 'UP')))
            # now we calculate the coordinates of potential point to go
            _x, _y = __dir.change_x(_bm.get_x()), __dir.change_y(_bm.get_y())
            # if there's no barrier at random point
            if not (self._board.is_barrier_at(_x, _y) or
                    self._board.is_future_blast_at(_x, _y)):
                # here we count the attempt to choose the way
                self._count += 1
                # and check whether it's not the one we just came from
                if not self._last == (_x, _y) or self._count > 5:
                    # but we will go back if there were no others twice
                    _direction = __dir.to_string()
                    self._last = _bm.get_x(), _bm.get_y()
                    self._count = 0
                    break
        else: # it seem that we are surrounded
            print("It's long time passed. Let's drop a bomb")
            _direction = Direction('ACT').to_string() # let's drop a bomb  :)
        return _direction
        
if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
