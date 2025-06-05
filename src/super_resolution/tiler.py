from typing import Tuple

import torch
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


def merge_tiles(tiles, output_size, scale, overlap):
    h_out, w_out = output_size[1] * scale, output_size[0] * scale
    result = torch.zeros(3, h_out, w_out)
    norm = torch.zeros(3, h_out, w_out)

    crop = overlap * scale // 2

    for (x, y), box, sr_tensor in tiles:
        sr_tensor = sr_tensor.squeeze(0).cpu()
        tile_h, tile_w = sr_tensor.shape[1:]

        sx, sy = x * scale, y * scale

        left = crop if sx > 0 else 0
        top = crop if sy > 0 else 0
        right = tile_w - crop if (sx + tile_w) < w_out else tile_w
        bottom = tile_h - crop if (sy + tile_h) < h_out else tile_h

        patch = sr_tensor[:, top:bottom, left:right]
        dst_x = sx + left
        dst_y = sy + top

        ph, pw = patch.shape[1:]
        if ph <= 0 or pw <= 0:
            continue

        result[:, dst_y:dst_y+ph, dst_x:dst_x+pw] += patch
        norm[:, dst_y:dst_y+ph, dst_x:dst_x+pw] += 1.0

    output = (result / norm.clamp(min=1e-8)).clamp(0.0, 1.0)
    return to_pil_image(output)