from typing import Tuple

from PIL import Image
from torchvision.transforms.functional import to_pil_image


def split_image_into_tiles(image: Image.Image, tile_size: int, overlap: int):
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
            tiles.append(((x, y), box, tile))
    return tiles, width, height


def merge_tiles(tiles: list, output_size: Tuple[int, int], scale: int, tile_size: int, overlap: int) -> Image.Image:
    output_image = Image.new('RGB', (output_size[0] * scale, output_size[1] * scale))
    for (x, y), box, tile in tiles:
        sr_tensor = tile
        sr_image = to_pil_image(sr_tensor.squeeze(0).cpu())
        sx, sy = x * scale, y * scale
        output_image.paste(sr_image, (sx, sy))
    return output_image
