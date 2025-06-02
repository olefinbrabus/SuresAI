# SuresAI 

---
## About The app
SuperResolution is a Python application for enhancing the resolution of images using the 
**EDSR (Enhanced Deep Super-Resolution)** model. It supports a command-line interface
and tile-based processing for handling large images efficiently.

---
## Technologies
- Python 3.13
- pillow
- Pytorch
- numpy
---
## Installing the application via Github
```bash
git clone  https://github.com/olefinbrabus/PopCornCinema
cd PopCornCinema
python -m venv venv
pip install -r requirements.txt
```
---
## Usage
```bash
python -m src.super_resolution.super_resolution \
  path/to/input.jpg \
  path/to/output.jpg
```