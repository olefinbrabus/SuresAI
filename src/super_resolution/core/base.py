from pathlib import Path
from types import SimpleNamespace

import torch
from numpy import ndarray
from torch import nn, Tensor
from torchvision.transforms.functional import to_tensor, to_pil_image

from src.super_resolution.core.model import edsr


def load_edsr_model() -> nn.Module:
    """Load a pre-trained EDSR model from Torch Hub.

    Returns:
        nn.Module: The EDSR model in evaluation mode.

    """
    model_path = Path(__file__).parent / 'model' / 'edsr_baseline_x4-6b446fab.pt'

    args = SimpleNamespace(
        scale=[4],
        n_resblocks=16,
        n_feats=64,
        res_scale=1,
        rgb_range=1.0,  # ← ключевое исправление
        n_colors=3
    )


    model = edsr.make_model(args)
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    model.eval()
    return model


def load_image(img_data: ndarray) -> Tensor:
    """Load an image from disk and convert it to a normalized 4D tensor.

    Args:
        img_data: Raster Dataset.

    Returns:
        Tensor: A 4D tensor (1, 3, H, W) with float values in [0.0, 1.0].

    """
    # img = Image.open(path).convert('RGB')
    img_tensor = to_tensor(img_data).unsqueeze(0) * 225.0
    return img_tensor


def apply_super_resolution(model: nn.Module, img_tensor: Tensor) -> Tensor:
    """Apply super-resolution to an image tensor using a pre-trained model.

    Args:
        model: The EDSR super-resolution model.
        img_tensor: The low-resolution input tensor [1, 3, H, W].

    Returns:
        Tensor: The high-resolution output tensor [1, 3, H', W'] with values clamped to [0.0, 1.0].

    """
    with torch.no_grad():
        sr_tensor = model(img_tensor).clamp(0.0, 225.0) / 225

    return sr_tensor


def save_image(tensor: Tensor, path: str) -> None:
    """Convert a tensor to a PIL image and save it to disk.

    Args:
        tensor: A 4D or 3D tensor representing an RGB image.
        path: Path where the output image will be saved.

    """
    img = to_pil_image(tensor.squeeze(0))
    img.save(path)

