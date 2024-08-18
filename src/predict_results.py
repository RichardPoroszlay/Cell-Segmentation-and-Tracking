from ultralytics import YOLO

# Load our custom YOLO model
model = YOLO("src/models/updated_model.pt")

source = "original_images"

model.predict(source, save=True, save_txt=True)
