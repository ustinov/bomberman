#! /usr/bin/env python3

from math import sqrt
from point import Point
from element import Element

class Board:
    """ Class describes the Board field for Bomberman game."""
    def __init__(self, board_string):
        self._string = board_string.replace('\n', '')
        self._len = len(self._string)  # the length of the string
        self._size = int(sqrt(self._len))  # size of the board 
        #print("Board size is sqrt", self._len, self._size)

    def _find_all(self, element):
        """ Returns the list of points for the given element type."""
        _points = []
        _a_char = element.get_char()
        for i, c in enumerate(self._string):
            if c == _a_char:
                 _points.append(self._strpos2pt(i))
        return _points

    def get_at(self, x, y):
        """ Return an Element object at coordinates x,y."""
        return Element(self._string[self._xy2strpos(x, y)])

    def is_at(self, x, y, element_object):
        """ Return True if Element is at x,y coordinates."""
        return element_object == self.get_at(x, y)

    def is_barrier_at(self, x, y):
        """ Return true if barrier is at x,y."""
        return Point(x, y) in self.get_barriers()

    def is_my_bomberman_dead(self):
        """ Returns False if your bomberman still alive."""
        return Element('DEAD_BOMBERMAN').getChar() in self._string

    def get_bomberman(self):
        """ Return the point where your bombermain is."""
        points = set()
        points.update(self._find_all(Element('BOMBERMAN')))
        points.update(self._find_all(Element('BOMB_BOMBERMAN')))
        points.update(self._find_all(Element('DEAD_BOMBERMAN')))
        assert len(points) <= 1, "There should be only one bomberman"
        return list(points)[0]

    def get_other_bombermans(self):
        """ Return the list of points for other bombermans."""
        points = set()
        points.update(self._find_all(Element('OTHER_BOMBERMAN')))
        points.update(self._find_all(Element('OTHER_BOMB_BOMBERMAN')))
        points.update(self._find_all(Element('OTHER_DEAD_BOMBERMAN')))
        return list(points)

    def get_meat_choppers(self):
        return self._find_all(Element('MEAT_CHOPPER'))

    def get_barriers(self):
        """ Return the list of barriers Points."""
        points = set()
        points.update(self.get_walls())
        points.update(self.get_bombs())
        points.update(self.get_destroy_walls())
        points.update(self.get_meat_choppers())
        points.update(self.get_other_bombermans())
        return list(points)
        
    def get_walls(self):
        """ Retuns the list of walls Element Points."""
        return self._find_all(Element('WALL'))

    def get_destroy_walls(self):
        """ """
        return  self._find_all(Element('DESTROY_WALL'))
        
    def get_bombs(self):
        """ Returns the list of bombs points."""
        points = set()
        points.update(self._find_all(Element('BOMB_TIMER_1')))
        points.update(self._find_all(Element('BOMB_TIMER_2')))
        points.update(self._find_all(Element('BOMB_TIMER_3')))
        points.update(self._find_all(Element('BOMB_TIMER_4')))
        points.update(self._find_all(Element('BOMB_TIMER_5')))
        points.update(self._find_all(Element('BOMB_BOMBERMAN')))
        return list(points)

    def get_blasts(self):
        return self._find_all(Element('BOOM'))

    def get_future_blasts(self):
        return self._f
        
    def is_near(self, x, y, elem):
        pass

    def count_near(self, x, y, elem):
        pass

    def to_string(self):
        return '\n'.join([self._string[i:i + self._size]
                              for i in range(0, self._len, self._size)])

    def _strpos2pt(self, strpos):
        return Point(*self._strpos2xy(strpos))

    def _strpos2xy(self, strpos):
        return (strpos % self._size, strpos // self._size)

    def _xy2strpos(self, x, y):
        return self._size * y + x
