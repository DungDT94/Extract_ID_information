import os
import xml.etree.ElementTree as ET
import numpy as np
import cv2
import glob


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

def get_center_point(coordinate_lst):
    lst = []
    for box in coordinate_lst:
        x_center = (float(box[0]) + float(box[2])) / 2
        y_center = (float(box[1]) + float(box[3])) / 2
        lst.append((x_center, y_center))
    return lst

def order_points(pts):
	rect = np.zeros((4, 2), dtype = "float32")
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	return rect

# ham nay co order point
def four_point_transform(image, pts):
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	return warped

# ham nay ko co order point
def four_point_transform_2(image, rect):
	#rect = order_points(pts)
	(tl, tr, br, bl) = rect
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	return warped


def process(folder_path, folder_save):
	for jpg_path in glob.glob(folder_path + '/*.jpg'):
		jpg_basename = os.path.basename(jpg_path)
		xml_path = jpg_path.split('.')[0] + '.xml'
		image = cv2.imread(jpg_path)
		coordinate = box_coordinate(xml_path)
		print(coordinate)
		center_coor = get_center_point(coordinate)
		print(center_coor)
		pts = np.array(center_coor, dtype = "float32")
		print(pts)
		warped = four_point_transform_2(image, pts)
		cv2.imwrite(folder_save + '/' + jpg_basename, warped)



if __name__ == "__main__":
	'''
	coordinate = box_coordinate('/home/dungdinh/Documents/prj_tach_chu_cccd/data_box_goc_xml/2d58a91a50254119a19ac1693f2722e6.xml')
	print(box_coordinate('/home/dungdinh/Documents/prj_tach_chu_cccd/data_box_goc_xml/0d9b99eaa7a54fad83a42a13804a361d.xml'))
	center_coor = get_center_point(coordinate)
	pts = np.array(center_coor, dtype="float32")
	print(pts)
	image = cv2.imread('/home/dungdinh/Documents/prj_tach_chu_cccd/data_box_goc_xml/2d58a91a50254119a19ac1693f2722e6.jpg')
	warped = four_point_transform(image, pts)
	cv2.imshow('transform', warped)
	cv2.waitKey(0)
	'''
	process('/home/dungdinh/Documents/prj_tach_chu_cccd/data_align_xml', '/home/dungdinh/Documents/prj_tach_chu_cccd/xoa')

