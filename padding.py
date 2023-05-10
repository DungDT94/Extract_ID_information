import glob
import cv2
import os
import numpy as np
from PIL import Image

# truyen vao file_path, tien hon khi generate
def padding(jpg_path):
    image = Image.open(jpg_path)
    width, height = image.size
    right = 20
    left = 20
    top = 20
    bottom = 20
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height), (0, 0, 0))
    result.paste(image, (left, top))
    return result

# truyen vao image, khi chay toan bo code
def padding_image(image):
    width, height = image.size
    right = 20
    left = 20
    top = 20
    bottom = 20
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height), (0, 0, 0))
    result.paste(image, (left, top))
    return result


def process(folder_path):
    for file in glob.glob(folder_path + '/*.jpg'):
        print(file)
        image = padding(file)
        image.save(file)

if __name__ == "__main__":
    process('/home/dungdinh/Documents/prj_tach_chu_cccd/box_goc_pad')


