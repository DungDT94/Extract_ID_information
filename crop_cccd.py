import os
import xml.etree.ElementTree as ET
import numpy as np
import cv2
import glob
import uuid

def box_coordinate(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    lst_all = []
    for bndbox in root.iter('bndbox'):
        lst_temp = []
        for i in range(4):
            lst_temp.append(bndbox[i].text)
        lst_all.append(lst_temp)
    return lst_all

def crop(folder, folder_save):
    for jpg_path in glob.glob(folder + '/*.jpg'):
        print(jpg_path)
        image = cv2.imread(jpg_path)
        xml_path = jpg_path.split('.')[0] + '.xml'
        lst_all = box_coordinate(xml_path)
        print(lst_all)
        for i in lst_all:
            crop_cccd =  image[int(i[1]):int(i[3]), int(i[0]):int(i[2])]
            cv2.imwrite(folder_save + '/' + uuid.uuid4().hex + '.jpg', crop_cccd)

if __name__ == "__main__":
    crop('/home/dungdinh/Documents/prj_tach_chu_cccd/newimage_background', '/home/dungdinh/Documents/prj_tach_chu_cccd/test')

