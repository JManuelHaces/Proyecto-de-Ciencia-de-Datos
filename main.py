import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from data.data import test_neumonia, test_normal, train_neumonia, train_normal
import functions as fn
import cv2
plt.style.use('ggplot')


# --------------- BALANCE INICIAL DE DATOS --------------- #
sets = {'test_neumonia':len(test_neumonia), 'test_normal':len(test_normal), 'train_neumonia':len(train_neumonia), 'train_normal':len(train_normal)}
per_train=np.round((sets['train_neumonia']+sets['train_normal'])/np.sum(list(sets.values())),4)*100

abs_train = sets['train_neumonia']+sets['train_normal']
abs_test = sets['test_neumonia']+sets['test_normal']
train_neumonia_prop = np.round(sets['train_neumonia']/abs_train,4)*100
test_neumonia_prop = np.round(sets['test_neumonia']/abs_test,4)*100