import os
import random

from PIL import Image
import glob
import uuid
import PIL

def add_image(image_path, back_ground_path):
    lst_scale = [2.5, 3, 3.5]
    lst_pos = [6, 7, 6.5]
    background = Image.open(back_ground_path)
    width_bg, height_bg = background.size
    image = Image.open(image_path)
    image_1 = image.rotate(90, PIL.Image.NEAREST, expand = 1)
    image_2 = image.rotate(180, PIL.Image.NEAREST, expand = 1)
    image_2 = image_2.resize((int(width_bg/random.choice(lst_scale)), int(width_bg/random.choice(lst_scale))))
    image_3 = image.rotate(270, PIL.Image.NEAREST, expand=1)
    image_3 = image_3.resize((int(width_bg/random.choice(lst_scale)), int(width_bg/random.choice(lst_scale))))
    #image_2 = image.rotate(, PIL.Image.NEAREST, expand=1)
    lst_image = [image, image_2, image_3, image_1]
    #image = image.resize((int(width_bg/random.choice(lst_scale)), int(width_bg/random.choice(lst_scale))))
    background.paste(random.choice(lst_image), (int(width_bg/random.choice(lst_pos)), int(height_bg/random.choice(lst_pos))))
    return background

if __name__ == "__main__":
    for background_path in glob.glob('background_2' + '/*'):
        for image_path in glob.glob('image_aligned_2' + '/*'):
            image = add_image(image_path, background_path)
            image.save('newimage_background/' + uuid.uuid4().hex + '.jpg')

