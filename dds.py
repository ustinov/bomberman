#!/usr/bin/env python3

from random import choice
from board import Board
from direction import Direction

class DirectionSolver:
    
    def __init__(self):
        
        self._direction = None
        self._bomb = None
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
        _direction = Direction('NULL')
        # here's how we find the current Point of our bomberman
        _bm = self._board.get_bomberman()
        print("Found your Bomberman at {}".format(_bm))
        #
        # here's how we get the list of barriers Points
        _barriers = self._board.get_barriers()
        while True:
            # here we get the random direction choise
            __dir = Direction(choice(('LEFT', 'RIGHT', 'DOWN', 'UP')))
            # now we calculate the coordinates of potential point to go
            _x, _y = __dir.change_x(_bm.get_x()), __dir.change_y(_bm.get_y())
            # if there's no barrier at random point
            if not self._board.is_barrier_at(_x, _y):
                # here we count the attempt to choose the way
                self._count += 1
                # and check whether it's not the one we just came from
                if not self._last == (_x, _y) or self._count > 5:
                    # but we will go back if there were no others twice
                    _direction = __dir.to_string()
                    self._last = _bm.get_x(), _bm.get_y()
                    self._count = 0
                    break
        return _direction
        
if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
