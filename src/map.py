# map.py  Class to represent the game map and the tiles it is made up of
# Paul Lockyer plockyer@googlemail.com
# 12th November 2020

class Map:
    """Represents a map for the game"""

    def __init__(self):
        """Standard class initializer"""

        # Internal dictionary of tiles that map up the map
        self.tiles = {}

    def add_tile(self, tile_object, x, y):
        """Adds a tile to the internal tile dictionary with the specified index"""
        self.tiles[(x, y)] = tile_object

    def valid_move(self, x, y):
        """Determines if the planned move is valid or not"""
        if not self.tiles[(x, y)]:
            return False
        else:
            return True
