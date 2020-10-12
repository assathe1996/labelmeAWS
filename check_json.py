#!/usr/bin/env python
import json
import os
import base64

total_points = 98
total_flags = 7

def check_json(filename):
    currentDirPath = os.getcwd()
    targetDirPath = os.path.join(currentDirPath, filename)

    # load the json file
    jsonFile=open(os.path.join(dataset_dir,file))
    jsonData=json.load(jsonFile)
    
    list_shapes=[]
    list_points=[]

    # landmarks and face bounding box should not empty and length of landmark points a
    # and face bounding box should be correct
    if len(jsonData["shapes"]) == 0:
        return True

    else:
        #Checking flags tag for length and null
        if not jsonData["flags"] or len(jsonData["flags"]) != total_flags: 
            return True

        for shape in jsonData["shapes"]:
            #Checking for length and null for landmarks and face bounding box
            list_shapes.append(shape["label"])
            if shape["shape_type"] == "rectangle" and shape["label"].lower()!="face":
                return True        
            if shape["shape_type"] == "rectangle":
                face_points_length = len(shape["points"])
                if face_points_length != 2:
                    return True
                if not shape["points"]:
                    return True
            if shape["shape_type"] == "point":
                point_points_length=len(shape["points"])
                if point_points_length != 1:
                    return True
                if not shape["points"]:
                    return True


        #Checking for duplicate entries and incomplete landmarks
        list_shapes_str = " ".join(list_shapes)
        list_points = [int(i) for i in list_shapes_str.split() if i.isdigit()]

        if len(list_shapes) != len(set(list_shapes)):  
            return True
        if len(list_points) != total_points and min(list_points) != 0 and max(list_points) != (total_points - 1): 
            return True

        for i in range(0, total_points):
            if i not in list_points:
                return True
        #Checking for null image data
        img_str = jsonData["imageData"]
        if img_str is None:
            return True
    return False          






