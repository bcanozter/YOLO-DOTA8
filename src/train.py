from ultralytics import YOLO


model = YOLO("yolo11n-obb.pt")

results = model.train(data="dota8.yaml", epochs=100, imgsz=640, val=True, verbose=True)
