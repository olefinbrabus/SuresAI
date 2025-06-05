import cv2
import numpy as np


def clahe_eq(img_bgr: np.ndarray) -> np.ndarray:
    """

    Args:
        img_bgr: np.ndarray

    Returns:
        np.ndarray

    """
    img_y_cr_cb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(img_y_cr_cb)

    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(16, 16))
    y_eq = clahe.apply(y)

    # y_eq = cv2.GaussianBlur(y_eq, (3, 3), 0)

    img_eq = cv2.merge((y_eq, cr, cb))
    return cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2BGR)

def suppress_saturation_hsv(img_rgb: np.ndarray, factor: float = 0.5) -> np.ndarray:
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(img_hsv)

    s = (s.astype(np.float32) * factor).clip(0, 255).astype(np.uint8)

    img_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

def reduce_contrast_hsv(img_rgb: np.ndarray, factor: float = 0.8) -> np.ndarray:
    assert img_rgb.dtype == np.uint8
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    v = v.astype(np.float32)
    mean = v.mean()
    v = (v - mean) * factor + mean
    v = np.clip(v, 0, 255).astype(np.uint8)

    hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

# test another method for avoiding artifacts
# def adjust_gamma(image: np.ndarray, gamma: float = 1.2) -> np.ndarray:
#     inv_gamma = 1.0 / gamma
#     table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
#     return cv2.LUT(image, table)