from ultralytics import YOLO
model = YOLO('/home/dungdinh/Documents/prj_tach_chu_cccd/model_corner/runs/detect/train/weights/last.pt')
model.train(data='box_cccd.yaml', epochs=100, imgsz=448, batch=4, device=0, save_period = 20)
