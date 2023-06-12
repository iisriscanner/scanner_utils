import re
import cv2
import base64, io
from PIL import Image
import numpy as np
from pathlib import Path


def image_to_base64(image, extension=None):
    BASE64_STR = base64.b64encode(image).decode("utf-8")
    if not extension:
        extension = "jpg"
    return f"data:image/{extension};base64,{BASE64_STR}"


def image_file_to_base64(image_path):
    IMAGE_EXTENSION = Path(image_path).suffix[1:]
    IMAGE = open(image_path, "rb").read()
    return image_to_base64(IMAGE, IMAGE_EXTENSION)


def base64_to_image(base64_data):
    META_DATA, BASE64_STR = base64_data.split(",")
    IMAGE_EXTENSION = re.search("/(.*);", META_DATA).group(1)
    binary_string = base64.b64decode(BASE64_STR)
    return Image.open(io.BytesIO(binary_string))


def base64_to_cv2image(base64_data, as_rgb=False):
    image = base64_to_image(base64_data)
    if as_rgb:
        return np.array(image)
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
