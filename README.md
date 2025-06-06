# SuresAI 

---
## About The app
SuperResolution is a Python application for enhancing the resolution of images using the 
**EDSR (Enhanced Deep Super-Resolution)** based on edsr_baseline_x4-6b446fab model. Application have tile-based processing for handling large images efficiently.

---
## Technologies
- Python 3.13
- pillow
- Pytorch
- numpy
- OpenCV

## Features
- Support Dataset learning
- Each photo in low-resolution_photos folder has been improved
---

## Original image (1,190x1,190 JPEG (24-bit color) 568,37 kB)
![plot](src/super_resolution/test_photos/IMG_2089_low.jpg)

## Improved image (4,760x4,760 JPEG (24-bit color) 2,73 MB)
![plot](src/super_resolution/test_photos/IMG_2089_high.jpg)

## Original image (3,264x2,448 JPEG (24-bit color) 2,1 MB)
![plot](src/super_resolution/test_photos/IMG_3283_low.jpg)

## Improved image (13,056x9,792 JPEG (24-bit color) 9,26 MB)
![plot](src/super_resolution/test_photos/IMG_3283_high.jpg)

## Original image (561x748 JPEG (24-bit color) 73,59 kE)
![plot](src/super_resolution/test_photos/IMG_6012_low.jpg)

## Improved image (2,244x2,992 JPEG (24-bit color) 312,68 kB)
![plot](src/super_resolution/test_photos/IMG_6012_high.jpg)

---
## Pixel difference
![plot](src/super_resolution/test_photos/img1.png)

![plot](src/super_resolution/test_photos/img2.png)

## In developing 
- support png format

---

## Installing the application via GitHub
```bash
git clone  https://github.com/olefinbrabus/PopCornCinema
cd PopCornCinema
python3 -m venv venv
pip install -r requirements.txt
```
---
## Usage
1. Transfer all the necessary photos to folder low-resolution_photos
2. Launch application:

```bash
python main.py
```

3. await photos
4. enjoy your photos :)