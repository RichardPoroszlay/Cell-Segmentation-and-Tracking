def add_suffixes_to_lines(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        # Loop through each line in the input file
        for line in lines:
            # Strip any extra whitespace or newlines from the line
            line = line.strip()

            # If the line is not empty, process it
            if line:
                # Base filename without extension
                base_filename = line.replace(".tif", "")

                # Define the suffixes
                suffixes = ["_top_left", "_top_right", "_bottom_left", "_bottom_right"]

                # Write the new lines with suffixes to the output file
                for suffix in suffixes:
                    new_line = base_filename + suffix + ".tif"
                    outfile.write(new_line + "\n")

# Example usage
input_file = "C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/cropped_cyprus_val_labels/old_train.txt"  # Input file with original .txt filenames
output_file = "C:/Users/Richard/Desktop/Cell-Segmentation-and-Tracking/cropped_cyprus_val_labels/train.txt"  # Output file where the new lines will be saved

add_suffixes_to_lines(input_file, output_file)