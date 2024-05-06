import os
import cv2

def rename_files(directory):
    files = os.listdir(directory)

    index = 1

    for filename in files:
        if filename.endswith(('.tif', '.tiff')):

            new_filename = f"{index:07d}_inv.tif"

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)

            index += 1

def rename__txt_files(folder_path, suffix):
    # Check if the folder exists
    if os.path.isdir(folder_path):
        # Iterate through each file in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is a text file
            if filename.endswith(".txt"):
                # Generate the new filename with the specified suffix appended
                new_filename = os.path.splitext(filename)[0] + suffix + ".txt"
                # Rename the file
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                print(f"Renamed: {filename} -> {new_filename}")
        print("All files renamed successfully.")
    else:
        print("Invalid folder path.")


def extract_center_coordinates(txt_files_directory):
    center_coordinates = []
    for i in range(1, 1801):  # Assuming you have 1800 files
        file_path = f"{txt_files_directory}/{'{:07d}'.format(i)}.txt"
        if(os.path.exists(file_path)):
            with open(file_path, 'r') as file:
                frame = []
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split()
                    classifier = parts[0]
                    center_x = float(parts[1])
                    center_y = float(parts[2])
                    frame.append((classifier, center_x, center_y))
                center_coordinates.append(frame)
        else:
            continue

    return center_coordinates


def normalize_coordinates(center_coordinates, image_width, image_height):
    normalized_coordinates = []
    for coordinates_list in center_coordinates:
        normalized_coordinates_list = [(classifier, int(center_x * image_width), int(center_y * image_height)) for classifier, center_x, center_y in coordinates_list]
        normalized_coordinates.append(normalized_coordinates_list)
    return normalized_coordinates


def invert_images(input_directory, output_directory):
    
    os.makedirs(output_directory, exist_ok=True)

    # Iterate over each file in the directory
    for filename in os.listdir(input_directory):
        # Read the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)

        if image is not None:
            # Apply bitwise NOT operation
            inverted_image = cv2.bitwise_not(image)

            # Write the modified image to the output directory
            output_path = os.path.join(output_directory, filename)
            cv2.imwrite(output_path, inverted_image)
            print(f"Processed: {filename}")
        else:
            print(f"Failed to read: {filename}")
