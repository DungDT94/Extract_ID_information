from ultralytics import YOLO
model = YOLO('yolov8m.pt')
model.train(data='box_cccd.yaml', epochs=200, imgsz=512, batch=4, device=0, save_period = 20)
