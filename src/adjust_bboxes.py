import os

def adjust_bbox(original_bbox, crop_origin, crop_size, original_size, overlap):
    obj_class, x_center, y_center, width, height = original_bbox

    # Denormalize the coordinates
    x_center = x_center * original_size[0]
    y_center = y_center * original_size[1]
    width = width * original_size[0]
    height = height * original_size[1]

    # Adjust based on crop origin and overlap
    crop_x, crop_y = crop_origin
    crop_width, crop_height = crop_size
    x_overlap, y_overlap = overlap

    # Calculate new coordinates relative to the crop
    x_center_new = (x_center - crop_x + x_overlap) / crop_width
    y_center_new = (y_center - crop_y + y_overlap) / crop_height

    # Normalize width and height
    width_new = width / crop_width
    height_new = height / crop_height

    # Ensure coordinates are still within the bounds
    if 0 <= x_center_new <= 1 and 0 <= y_center_new <= 1:
        return [obj_class, x_center_new, y_center_new, width_new, height_new]
    else:
        return None

def process_annotations(input_dir, output_dir, crop_params, original_size, overlap):
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, 'r') as f:
                annotations = f.readlines()

            for crop_name, crop_origin, crop_size in crop_params:
                output_annotations = []
                for annotation in annotations:
                    annotation = annotation.strip().split()
                    obj_class = int(annotation[0])
                    bbox = list(map(float, annotation[1:]))
                    adjusted_bbox = adjust_bbox([obj_class] + bbox, crop_origin, crop_size, original_size, overlap)
                    if adjusted_bbox:
                        output_annotations.append(" ".join(map(str, adjusted_bbox)))

                # Write the adjusted annotations to new file
                output_filename = filename.replace(".txt", f"_{crop_name}.txt")
                output_path = os.path.join(output_dir, output_filename)
                with open(output_path, 'w') as out_f:
                    out_f.write("\n".join(output_annotations))

# Example usage
input_dir = "C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/merged-dataset/labels/train"  # Folder with original YOLO annotations
output_dir = "C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/cropped_cyprus_val_labels/obj_train_data"  # Where to save the new cropped annotations

# Original image size (width, height)
original_size = (1300, 1030)

# Crop parameters: (crop_name, crop_origin (x, y), crop_size (width, height))z
crop_params = [
    ("top_left", (0, 0), (700, 565)),
    ("top_right", (600, 0), (700, 565)),
    ("bottom_left", (0, 465), (700, 565)),
    ("bottom_right", (600, 465), (700, 565)),
]

# Overlap (x_overlap, y_overlap) in pixels
overlap = (0, 0)

process_annotations(input_dir, output_dir, crop_params, original_size, overlap)