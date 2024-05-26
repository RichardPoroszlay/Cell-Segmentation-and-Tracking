import numpy as np
import open3d as o3d
import utils.utils

height = 600 # height of frames
width = 800 # width of frames
depth = 1800 # number of frames

center_coordinates = utils.utils.extract_center_coordinates("runs/detect/predict/labels")

normalized_coordinates = utils.utils.normalize_coordinates(center_coordinates, width, height)

'''
point_data = np.random.rand(100, 3)

print(point_data)
'''

point_data = []

for frame_idx, coordinates_list in enumerate(normalized_coordinates, start=1):
     for coordinates_tuple in coordinates_list:
        classifier, center_x, center_y = coordinates_tuple

        point_data.append([center_x, center_y, frame_idx])

print(point_data)

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
