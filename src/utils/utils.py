import os


def rename_files(directory):
    files = os.listdir(directory)

    index = 1

    for filename in files:
        if filename.endswith(('.tif', '.tiff')):

            new_filename = f"{index:07d}.tif"

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)

            index += 1


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
