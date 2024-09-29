import os
import cv2


def crop_image_with_overlap(image, overlap_x=0, overlap_y=0):
    """
    Crops the image into four overlapping pieces.
    """
    height, width, _ = image.shape

    mid_x = width // 2
    mid_y = height // 2

    mid_x_left = max(mid_x - overlap_x, 0)
    mid_x_right = min(mid_x + overlap_x, width)
    mid_y_top = max(mid_y - overlap_y, 0)
    mid_y_bottom = min(mid_y + overlap_y, height)

    top_left = image[:mid_y_bottom, :mid_x_right]
    top_right = image[:mid_y_bottom, mid_x_left:]
    bottom_left = image[mid_y_top:, :mid_x_right]
    bottom_right = image[mid_y_top:, mid_x_left:]

    return top_left, top_right, bottom_left, bottom_right


def process_directory(input_directory, output_directory, overlap_x=0, overlap_y=0):
    """
    Processes all images in the input directory, applies cropping with overlap,
    and saves them with the original names appended with corner labels.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(('.tif', '.tiff', '.jpg')):
            file_path = os.path.join(input_directory, filename)

            image = cv2.imread(file_path)
            if image is None:
                print(f"Skipping {filename}, as it's not a valid image.")
                continue

            top_left, top_right, bottom_left, bottom_right = crop_image_with_overlap(image, overlap_x, overlap_y)

            # Get the base name without the extension
            base_name, ext = os.path.splitext(filename)

            output_top_left = os.path.join(output_directory, f"{base_name}_top_left{ext}")
            output_top_right = os.path.join(output_directory, f"{base_name}_top_right{ext}")
            output_bottom_left = os.path.join(output_directory, f"{base_name}_bottom_left{ext}")
            output_bottom_right = os.path.join(output_directory, f"{base_name}_bottom_right{ext}")

            cv2.imwrite(output_top_left, top_left)
            cv2.imwrite(output_top_right, top_right)
            cv2.imwrite(output_bottom_left, bottom_left)
            cv2.imwrite(output_bottom_right, bottom_right)

            print(f"Processed and saved: {filename}")


input_directory = 'C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/merged-dataset/images/val'
output_directory = 'cropped_cyprus_val'
process_directory(input_directory, output_directory, overlap_x=50, overlap_y=50)
