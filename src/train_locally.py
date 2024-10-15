import os

from ultralytics import YOLO

ROOT_DIR = "root-dir"

# Load a model
model = YOLO("yolov8x.pt")  # load pre trained model

# Use the model
results = model.train(data=os.path.join(ROOT_DIR, "config.yaml"), epochs=100)  # train the model
