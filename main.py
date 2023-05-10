from model_cccd.yolov8_model import *
from model_corner.yolov8_model import DetectCorner
from padding import *
from perspective_transform import *
from crop_cccd import *
import cv2
from PIL import Image
import numpy as np


class Extract:
    def __init__(self):
        self.model_cccd = YOLOv8()
        self.model_corner = DetectCorner()

    def align(self, image_p):
        lst_all = self.model_cccd.predict(image_p)
        image_pil = Image.open(image_p)
        print(lst_all)
        for i in lst_all:
            crop = image_pil.crop((i[0], i[1], i[2], i[3]))
            crop_pad_pil = padding_image(crop)
            crop_pad_cv2 = cv2.cvtColor(np.array(crop_pad_pil), cv2.COLOR_RGB2BGR)
            #cv2.imshow('cv2', crop_pad_cv2)
            #cv2.waitKey(0)
            crop_pad_pil.show()
            coor_corner= self.model_corner.predict(crop_pad_pil)
            # print(coor_corner)
            coor_center = get_center_point(coor_corner)
            # print(coor_center)
            pts = np.array(coor_center, dtype="float32")
            # print(pts)
            warped = four_point_transform_2(crop_pad_cv2, pts)
            cv2.imshow('aligned', warped)
            cv2.waitKey(0)



if __name__ == "__main__":
    model = Extract()
    model.align('/home/dungdinh/Documents/prj_tach_chu_cccd/data_test_cccd/a6fd69dcfe494af49dbc8c86514d2005.jpg')

