#!/usr/bin/env python3
from PIL import Image
import os
# from pathlib import Path

source_dir = "" # enter the path to the folder containing the images to be changed here
target_dir = "" # enter the path to the folder that will contain the edited images here

# create target directory
# Path("/my/directory").mkdir(parents=True, exist_ok=True)

# list all files in the target directory and iterate through them
for current_image in os.listdir(source_dir):

    # check whether the current file is actually an image
    if current_image != ".DS_Store":

        # open a single image
        im = Image.open(os.path.join(source_dir,current_image)).convert('RGB')

        # rotate image by -90 degrees and resize images
        im = im.resize((128,128)).rotate(90)

        # save edited image
        im.save(os.path.join(target_dir,current_image),"JPEG")
        print(current_image)