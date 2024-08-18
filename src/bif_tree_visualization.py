import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import utils.utils

height = 600 # height of frames
width = 800 # width of frames
depth = 10 # number of frames

center_coordinates = utils.utils.extract_center_coordinates("runs/detect/predict/labels")

normalized_coordinates = utils.utils.normalize_coordinates(center_coordinates, width, height)

print(normalized_coordinates)

empty_3d_matrix = np.empty((height, width, depth))

print("Shape of the empty 3D matrix:", empty_3d_matrix.shape)

for frame_idx, coordinates_list in enumerate(normalized_coordinates):
    for coordinates_tuple in coordinates_list:
        classifier, center_x, center_y = coordinates_tuple
        if frame_idx < empty_3d_matrix.shape[2] and classifier == '0':
            empty_3d_matrix[center_y, center_x, frame_idx] = 1
        elif frame_idx < empty_3d_matrix.shape[2] and classifier == '1':
            empty_3d_matrix[center_y, center_x, frame_idx] = 2
            
# Visualize the 3D matrix
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_indices, y_indices, z_indices = np.where(empty_3d_matrix == 1)
ax.scatter(x_indices, y_indices, z_indices, c='r', marker='o', label="Cell")

x_indices, y_indices, z_indices = np.where(empty_3d_matrix == 2)
ax.scatter(x_indices, y_indices, z_indices, c='b', marker='o', label="Cell Division")

ax.set_xlabel('X (Height)')
ax.set_ylabel('Y (Width)')
ax.set_zlabel('Z (Num of frames)')

ax.legend()

plt.show()
