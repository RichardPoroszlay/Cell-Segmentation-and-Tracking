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


def rename_cyprus_data(directory):
    files = os.listdir(directory)

    for filename in files:
        if filename.endswith(('.tif', 'tiff')):
            new_filename = filename.replace('.tif', '_inv.tif')

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)

        elif filename.endswith(('.jpg')):

            new_filename = filename.replace('.jpg', '_inv.jpg')

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)

def rename_txt_files(folder_path, suffix):
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
        normalized_coordinates_list = [(classifier, int(center_x / 2 * image_width), int(center_y / 2 * image_height)) for classifier, center_x, center_y in coordinates_list]
        normalized_coordinates.append(normalized_coordinates_list)
    return normalized_coordinates


def invert_images_in_directory(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if the file is an image (assuming common image extensions)
        if filepath.lower().endswith(('.tif', '.tiff')):
            # Read the grayscale image
            image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            
            # Invert the image
            inverted_image = cv2.bitwise_not(image)
            
            # Save the inverted image back to the same file
            cv2.imwrite(filepath, inverted_image)

        elif filepath.lower().endswith(('.jpg')):
            # Read the grayscale image
            image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            
            # Invert the image
            inverted_image = cv2.bitwise_not(image)
            
            # Save the inverted image back to the same file
            cv2.imwrite(filepath, inverted_image)


def modify_yolo_files(directory):
    # Iterate through each file in the given directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            
            # Read the lines from the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Process each line according to the rules
            modified_lines = []
            for line in lines:
                parts = line.strip().split()
                
                # Ensure there are enough parts in the line before attempting to modify
                if len(parts) > 0:
                    first_value = int(parts[0])
                    # Apply the rules
                    if first_value == 1:
                        parts[0] = '3'
                    elif first_value == 2:
                        parts[0] = '1'
                    elif first_value == 3:
                        parts[0] = '2'
                
                # Join the parts back into a line
                modified_line = ' '.join(parts)
                modified_lines.append(modified_line)

            # Write the modified lines back to the file
            with open(file_path, 'w') as file:
                file.write('\n'.join(modified_lines))


def append_inv_paths(file_path):
    # Read the file paths from the text file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # List to store both original and modified file paths
    modified_lines = []

    for line in lines:
        # Remove any leading/trailing whitespace characters
        line = line.strip()

        # Ensure the line is not empty
        if line:
            # Add the original line to the modified lines list
            modified_lines.append(line)

            # Split the path to get directory and filename
            directory, filename = os.path.split(line)

            # Insert '_inv' before the file extension
            if '.' in filename:
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_inv{ext}"
            else:
                # If the file has no extension, just add _inv at the end
                new_filename = f"{filename}_inv"

            # Construct the new file path
            new_file_path = os.path.join(directory, new_filename)

            # Add the modified line to the list
            modified_lines.append(new_file_path)

    # Write all lines (original and modified) back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(modified_lines))


def change_cyprus_classification_to_our(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            
            # Read the file contents
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Open the file in write mode to overwrite it
            with open(file_path, 'w') as file:
                for line in lines:
                    parts = line.split()
                    if parts:  # Ensure the line is not empty
                        first_value = int(parts[0])
                        
                        if first_value == 1 or first_value == 2:
                            parts[0] = '1'
                            file.write(" ".join(parts) + '\n')
                        elif first_value != 3:
                            file.write(line)  # Write the line as is if the first value is not 4

    print("Files have been processed.")


def change_every_class_to_zero(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()

            modified_lines = []
            for line in lines:
                parts = line.strip().split()
                
                if len(parts) > 0:
                    parts[0] = '0'
                
                modified_line = ' '.join(parts)
                modified_lines.append(modified_line)

            with open(file_path, 'w') as file:
                file.write('\n'.join(modified_lines))


def clean_files(txt_folder, img_folder):
    deleted_images_count = 0
    deleted_files_count = 0
    
    for file in os.listdir(txt_folder):
        if file.endswith(".txt"):
            txt_path = os.path.join(txt_folder, file)
            
            with open(txt_path, "r") as txt_file:
                lines = txt_file.readlines()
            
            if len(lines) < 5:
                image_name = os.path.splitext(file)[0]
                tif_path = os.path.join(img_folder, f"{image_name}.tif")
                jpg_path = os.path.join(img_folder, f"{image_name}.jpg")
                
                os.remove(txt_path)
                deleted_files_count += 1
                print(f"Deleted {file} from txt folder")
                
                if os.path.exists(tif_path):
                    os.remove(tif_path)
                    deleted_images_count += 1
                    print(f"Deleted {image_name}.tif from image folder")
                elif os.path.exists(jpg_path):
                    os.remove(jpg_path)
                    deleted_images_count += 1
                    print(f"Deleted {image_name}.jpg from image folder")
                else:
                    print(f"No associated image found for {file}")
    
    print(f"\nOperation complete. Deleted {deleted_files_count} text files and {deleted_images_count} images.")
