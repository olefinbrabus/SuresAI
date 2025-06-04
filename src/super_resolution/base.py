import cv2
import numpy as np

from PIL import Image

from src.super_resolution.core.base import load_edsr_model, load_image, apply_super_resolution, save_image
from src.super_resolution.histogram_equalization import clahe_eq
from src.super_resolution.tiler import split_image_into_tiles, merge_tiles


def open_image(path: str) -> Image:
    """Open an image file, carries out flexible equalization of histogram and convert it to RGB.

    Args:
        path: Path to the image.

    Returns:
        PIL.Image.Image: RGB image.

    """
    Image.MAX_IMAGE_PIXELS = None
    image = Image.open(path).convert('RGB')
    image_array = np.array(image)

    image_bgr: np.ndarray = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    image_bgr_clahe = clahe_eq(image_bgr)
    image_rgb_clahe = cv2.cvtColor(image_bgr_clahe, cv2.COLOR_BGR2RGB)

    return Image.fromarray(image_rgb_clahe)

def super_resolution(src_filepath: str, dst_filepath: str, scale: int = 4, tile_size: int = 128, overlap: int = 16) -> None:
    img_data = open_image(src_filepath)
    tiles, width, height = split_image_into_tiles(img_data, tile_size, overlap)
    model = load_edsr_model()

    processed_tiles = []
    for (x, y), box, tile in tiles:
        img_tensor = load_image(tile)
        sr_tensor = apply_super_resolution(model, img_tensor)
        processed_tiles.append(((x, y), box, sr_tensor))

    sr_image = merge_tiles(processed_tiles, (width, height), scale, tile_size, overlap)
    sr_image.save(dst_filepath)