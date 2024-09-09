import os

from ultralytics import YOLO

ROOT_DIR = "C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/src/"

# Load a model
model = YOLO("yolov8l.pt")  # load pre trained model

# Use the model
results = model.train(data=os.path.join(ROOT_DIR, "config.yaml"), imgsz=1030 ,epochs=50)  # train the model
# results = model.train(data=os.path.join(ROOT_DIR, "config.yaml"), imgsz=(1300, 1030) ,epochs=50)  # train the model
