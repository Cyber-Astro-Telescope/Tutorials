import bpy
import pyopenvdb as vdb
import numpy as np

# Please define a root folder and a file name
# **It is necessary to have a root since you do not have permission to write in Blender folder
root = "Fill/In/Your/Root/Path/Here/"
file = "example.npz"

def clear_scene():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def load_data(path):
    # Use any methods to load the density field data
    # The shape of the data should be ( x , x , x) where x is the resolution
    # For example, use numpy.load() to load the data from a .npz file as the following:
    data = np.load(path)
    
    return data["arr_0"]


def normalize_density(data, intensity):
    # normalize
    data_norm = (data)/(data.max() - data.min()) * intensity
    return data_norm

def create_grid(data, name):
    grid = vdb.FloatGrid()
    grid.name = name
    grid.copyFromArray(data)
    return grid

def load_vdb(name):
    bpy.ops.object.volume_import(filepath=name, directory=root, files=[{"name":name, "name":name}], relative_path=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# Remove all the object in default Blender
clear_scene()

data = load_data(root + file)

# Normalize data, you can change the intensity value but not lower value might not be very visible
# If you know how to change density in GUI, leave the intensity to be 1
data_norm = normalize_density(data, 100)

# Create the grid for vdb file format
grid = create_grid(data_norm, "density")

# This is for normalzing the size of the grid
# Not necessary, but it is recommended
grid.transform = vdb.createLinearTransform(voxelSize=1/(data.shape[0])*5)

vdb.write(root + "example.vdb", grids = [grid])

load_vdb("example.vdb")
