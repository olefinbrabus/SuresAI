from PIL import Image

from src.super_resolution.core.base import load_edsr_model, load_image, apply_super_resolution, save_image


def open_image(path: str) -> Image:
    """Open an image file and convert it to RGB.

    Args:
        path: Path to the image.

    Returns:
        PIL.Image.Image: RGB image.

    """
    return Image.open(path).convert('RGB')


def super_resolution(src_filepath: str, dst_filepath: str, scale: int = 4) -> None:
    """Run EDSR super-resolution on a single image.

    Args:
        src_filepath (str): Path to the input image.
        dst_filepath (str): Path to save the output image.
        scale (int): Upscaling factor (2, 3, or 4).

    """

    img_data = open_image(src_filepath)
    model = load_edsr_model()
    img_tensor = load_image(img_data)
    sr_tensor = apply_super_resolution(model, img_tensor)
    save_image(sr_tensor, dst_filepath)
