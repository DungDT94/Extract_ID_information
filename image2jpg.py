from PIL import Image
import os
import uuid

def png2jpg(folder_image):
    for file in os.listdir(folder_image):
        if file.endswith((".png", ".jpg", ".jpeg")):
            path_file = os.path.join(folder_image, file)
            img = Image.open(path_file)
            img.save(uuid.uuid4().hex + '.jpg')
            os.remove(path_file)

if __name__ == "__main__":
    png2jpg('/home/dungdinh/Documents/prj_tach_chu_cccd/data/')
