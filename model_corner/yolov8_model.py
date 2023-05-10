from ultralytics import YOLO
import numpy as np
import cv2


class DetectCorner:
    def __init__(self):
        self.model = YOLO('/home/dungdinh/Documents/prj_tach_chu_cccd/model_corner/runs/detect/train2/weights/best.pt')

    def predict(self, img):
        result = self.model(source=img, show=True)
        #cv2.waitKey(0)

        boxes = result[0].boxes
        list_box = []
        dict = {}
        for box in boxes:
            label = box.cls.tolist()[0]
            box2list = box.xyxy.tolist()
            #print(box2list)
            box2list = np.reshape(box2list, (4,))
            #print(box2list)
            box2list = box2list.tolist()
            #print(box2list)
            dict[label] = box2list

            #list_box.append(box2list)
        print(dict)

        list_box.append(dict[0.0])
        list_box.append(dict[1.0])
        list_box.append(dict[2.0])
        list_box.append(dict[3.0])
        print(list_box)
        return list_box



if __name__ == "__main__":
    model = DetectCorner()
    image = cv2.imread('/home/dungdinh/Documents/prj_tach_chu_cccd/background_newimage/0c6b775eff9f4ff6a058f207073e16fb.jpg')
    lst = model.predict('/home/dungdinh/Documents/prj_tach_chu_cccd/data_test_cccd/a5bc9f903e0142dabacc3b14ee184dc4.jpg')
    #print(lst)
