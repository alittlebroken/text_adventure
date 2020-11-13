# tiles.py Tile class and tile objects used in the game maps
# Paul Lockyer plockyer@googlemail.com
# 13th November 2020

class Tile:
    """Tile object"""

    def __init__(self, name, content='', symbol=''):
        """Standard class initializer"""
        self.name = name
        self.content = content
        self.symbol = symbol


# Some basic tiles
water_tile = Tile('Water', '', '~')
wood_tile =  Tile('Wood', '', '^')
entry_tile = Tile('Enter', '', '@<')
exit_tile = Tile('Exit', '', '@>')



