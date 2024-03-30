from ultralytics import YOLO

# Load our custom-trained YOLOv8s model
model = YOLO("src/models/cell_and_div_model_epoch100_medium_best.pt")

source = "cell_dataset"

model.predict(source, save=True, save_txt=True, conf=0.5)
