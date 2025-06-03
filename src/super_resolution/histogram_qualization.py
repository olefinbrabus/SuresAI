import cv2


def clahe_eq(img_bgr):
    img_y_cr_cb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(img_y_cr_cb)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    y_eq = clahe.apply(y)

    img_eq = cv2.merge((y_eq, cr, cb))
    return cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2BGR)