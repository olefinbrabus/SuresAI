from typing import Tuple

from PIL import Image


def split_image_into_tiles(image: Image.Image, tile_size: int, overlap: int) -> Tuple[list, int, int]:
    """Split an image into overlapping tiles.

    Returns:
        tiles: List of cropped image tiles.
        cols: Number of tiles horizontally.
        rows: Number of tiles vertically.

    """
    width, height = image.size
    tiles = []
    for y in range(0, height, tile_size - overlap):
        for x in range(0, width, tile_size - overlap):
            box = (x, y, min(x + tile_size, width), min(y + tile_size, height))
            tile = image.crop(box)
            tiles.append(((x, y), tile))
    return tiles, width, height
