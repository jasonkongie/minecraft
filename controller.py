import json
from mcpi.minecraft import Minecraft

class MinecraftController:
    def __init__(self):
        """Initialize the Minecraft game connection."""
        self.mc = Minecraft.create()
        # Load block IDs from JSON
        with open("blocks.json", "r") as file:
            self.blocks = json.load(file)

    def build_house(self, width, length, height, x_offset=0, y_offset=0, z_offset=0):
        """Builds a simple house with specified dimensions and relative position."""
        base_pos = self.mc.player.getTilePos()
        base_pos.x += x_offset
        base_pos.y += y_offset
        base_pos.z += z_offset

        # Using block IDs from the loaded JSON
        wood_planks_id = self.blocks["WOOD_PLANKS"]
        glass_id = self.blocks["GLASS"]
        door_wood_id = self.blocks["DOOR_WOOD"]

        # Build walls
        for x in range(width):
            for y in range(height):
                for z in range(length):
                    if x == 0 or x == width - 1 or z == 0 or z == length - 1 or y == 0 or y == height - 1:
                        self.mc.setBlock(base_pos.x + x, base_pos.y + y, base_pos.z + z, wood_planks_id)

        # Add a door
        door_x = base_pos.x + width // 2
        self.mc.setBlock(door_x, base_pos.y, base_pos.z, door_wood_id)
        self.mc.setBlock(door_x, base_pos.y + 1, base_pos.z, door_wood_id)  # Top part of the door

        # Add windows
        window_y = base_pos.y + height // 2
        for z in range(1, length - 1):
            if z % 2 == 1:  # Add windows on both sides of the house
                self.mc.setBlock(base_pos.x, window_y, base_pos.z + z, glass_id)
                self.mc.setBlock(base_pos.x + width - 1, window_y, base_pos.z + z, glass_id)

        # Add a flat roof
        for x in range(width):
            for z in range(length):
                self.mc.setBlock(base_pos.x + x, base_pos.y + height, base_pos.z + z, wood_planks_id)


    def go_up(self, blocks):
        """Move the player up by a specified number of blocks."""
        pos = self.mc.player.getTilePos()
        self.mc.player.setTilePos(pos.x, pos.y + blocks, pos.z)

    def go_down(self, blocks):
        """Move the player down by a specified number of blocks."""
        pos = self.mc.player.getTilePos()
        self.mc.player.setTilePos(pos.x, pos.y - blocks, pos.z)

    def walk_north(self, blocks):
        """Move the player north by a specified number of blocks."""
        pos = self.mc.player.getTilePos()
        self.mc.player.setTilePos(pos.x, pos.y, pos.z - blocks)

    def walk_south(self, blocks):
        """Move the player south by a specified number of blocks."""
        pos = self.mc.player.getTilePos()
        self.mc.player.setTilePos(pos.x, pos.y, pos.z + blocks)

    def walk_east(self, blocks):
        """Move the player east by a specified number of blocks."""
        pos = self.mc.player.getTilePos()
        self.mc.player.setTilePos(pos.x + blocks, pos.y, pos.z)

    def walk_west(self, blocks):
        """Move the player west by a specified number of blocks."""
        pos = self.mc.player.getTilePos()
        self.mc.player.setTilePos(pos.x - blocks, pos.y, pos.z)

    def place_block(self, block_type, x_offset=0, y_offset=0, z_offset=0):
        """Place a block relative to the player's current position."""
        pos = self.mc.player.getTilePos()
        self.mc.setBlock(pos.x + x_offset, pos.y + y_offset, pos.z + z_offset, block_type)

    def remove_block(self, x_offset=0, y_offset=0, z_offset=0):
        """Remove a block relative to the player's current position."""
        air_id = self.get_block_id("AIR")
        pos = self.mc.player.getTilePos()
        self.mc.setBlock(pos.x + x_offset, pos.y + y_offset, pos.z + z_offset, air_id)

    def build_column(self, block_type, height):
        """Build a vertical column of blocks above the player."""
        pos = self.mc.player.getTilePos()
        for i in range(height):
            self.mc.setBlock(pos.x, pos.y + i, pos.z, block_type)

    def dig_down(self, depth):
        """Remove blocks under the player up to a specified depth."""
        pos = self.mc.player.getTilePos()
        for i in range(depth):
            self.mc.setBlock(pos.x, pos.y - i, pos.z, AIR)


