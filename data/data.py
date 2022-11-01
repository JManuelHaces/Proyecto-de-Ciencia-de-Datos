import os
import zipfile
from PIL import Image
import glob
import matplotlib.pyplot as plt
import functions as fn
import numpy as np

# Function to extract data
def extract_data():
    zip_ref = zipfile.ZipFile('data/chest_xray.zip', 'r')
    zip_ref.extractall('data/data_chest_xray')
    zip_ref.close()
#extract_data()

# function to load images
def load_images(folder):
    image_list = []
    for filename in glob.glob(f'{folder}//*.jpeg'): 
        im=Image.open(filename)
        image_list.append(im)
    return image_list

# Load images

test_normal = load_images('data/data_chest_xray/test/NORMAL')
test_neumonia = load_images('data/data_chest_xray/test/PNEUMONIA')
train_normal = load_images('data/data_chest_xray/train/NORMAL')
train_neumonia = load_images('data/data_chest_xray/train/PNEUMONIA')


# --------------- Resize the images & make them flatten --------------- # 

# Resize
test_normal = [img.resize((350,350)) for img in test_normal]
test_neumonia = [img.resize((350,350)) for img in test_neumonia]
train_normal = [img.resize((350,350)) for img in train_normal]
train_neumonia = [img.resize((350,350)) for img in train_neumonia]

# Matrix format
test_normal = fn.matrix_format(test_normal)
test_neumonia = fn.matrix_format(test_neumonia)
train_normal = fn.matrix_format(train_normal)
train_neumonia = fn.matrix_format(train_neumonia)

# --------------- Normalize --------------- #

max_train_neumonia = np.max([np.max(i) for i in train_neumonia])
max_train_normal = np.max([np.max(i) for i in train_normal])

# The maximum is 255, so let's devide everythin by this number

# test_normal = [ a/255 for a in test_normal] 
# test_neumonia = [ a/255 for a in test_neumonia]
# train_normal = [ a/255 for a in train_normal]
# train_neumonia = [ a/255 for a in train_neumonia]

