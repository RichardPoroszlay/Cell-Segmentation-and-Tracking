import os

from ultralytics import YOLO

ROOT_DIR = "C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/src/"

# Load a model
model = YOLO("yolov8x-p2.yaml").load("yolov8x.pt")  # load pre trained model

# Use the model
results = model.train(data=os.path.join(ROOT_DIR, "config.yaml"), imgsz=1030, epochs=100)  # train the model
# results = model.train(data=os.path.join(ROOT_DIR, "config.yaml"), imgsz=(1030, 1300), epochs=100)  # train the model
