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

# test another method for avoiding artifacts
# def adjust_gamma(image: np.ndarray, gamma: float = 1.2) -> np.ndarray:
#     inv_gamma = 1.0 / gamma
#     table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
#     return cv2.LUT(image, table)