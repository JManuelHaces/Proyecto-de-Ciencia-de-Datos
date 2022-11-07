import os
import zipfile
from PIL import Image
import glob
import matplotlib.pyplot as plt

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



test_normal = load_images('data/data_chest_xray/test/NORMAL')
test_neumonia = load_images('data/data_chest_xray/test/PNEUMONIA')
train_normal = load_images('data/data_chest_xray/train/NORMAL')
train_neumonia = load_images('data/data_chest_xray/train/PNEUMONIA')





