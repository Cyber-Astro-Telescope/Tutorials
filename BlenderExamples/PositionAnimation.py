# This script is used to create an animation of a object when you have the position 
# of the object in each frame

import numpy as np
import bpy

# Select a object in the scene and use it to visualize the object
object_name = "Cube"
obj = bpy.data.objects.get(object_name)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Deselect all other objects
for ob in bpy.context.selected_objects:
    if ob.name != object_name:
        ob.select_set(False)

# Load the object position 
Positions = np.load("PATH\TO\YOUR\FILE")

# Set the start and end of the animation
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = len(Positions) - 1

for frame_number, position in enumerate(Positions):
    # Set the cube location the 256*5 is for normalization, you shoud change it if this is not your case!
    obj.location = position/256*5
    # Insert a keyframe for location at each frame
    obj.keyframe_insert(data_path="location", frame=frame_number)