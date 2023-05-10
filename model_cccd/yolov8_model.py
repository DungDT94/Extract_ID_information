from ultralytics import YOLO
import numpy as np
import cv2


class YOLOv8:
    def __init__(self):
        self.model = YOLO('/home/dungdinh/Documents/prj_tach_chu_cccd/model_cccd/runs/detect/train_data_box_sat/weights/best.pt')

    def predict(self, img):
        result = self.model(source=img, show=True)

        boxes = result[0].boxes
        list_box = []
        for box in boxes:
            temp_list = []
            box2list = box.xyxy.tolist()
            box2list = np.reshape(box2list, (4,))
            box2list = box2list.tolist()
            list_box.append(box2list)
        return list_box
            


if __name__ == "__main__":
    model = YOLOv8()
    image = cv2.imread('/home/dungdinh/Documents/prj_tach_chu_cccd/background_newimage/0c6b775eff9f4ff6a058f207073e16fb.jpg')
    lst = model.predict('/home/dungdinh/Documents/prj_tach_chu_cccd/newimage_background/0b9b2db476da4a34badb18d7f6b35b01.jpg')
    print(lst)
    #print(lst)
