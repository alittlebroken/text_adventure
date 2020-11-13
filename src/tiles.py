# tiles.py Tile class and tile objects used in the game maps
# Paul Lockyer plockyer@googlemail.com
# 13th November 2020

class Tile:
    """Tile object"""

    def __init__(self, name, content=''):
        """Standard class initializer"""
        self.name = name
        self.content = content


# Game tiles
tile_town_hall = Tile('Town Hall', '')
tile_post_office = Tile('Post Office', '')
tile_common = Tile('Village Green', '')
tile_pub = Tile('Fox and Hound Pub', '')
tile_farm = Tile('OakPastures Farm', '')
tile_road = Tile('Road', '')
tile_train_station = Tile('Train Station', '')
