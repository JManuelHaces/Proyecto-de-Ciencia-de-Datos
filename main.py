from pyexpat import model
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from data.data import test_neumonia, test_normal, train_neumonia, train_normal
import functions as fn
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
plt.style.use('ggplot')


# --------------- BALANCE INICIAL DE DATOS --------------- #
sets = {'test_neumonia':len(test_neumonia), 'test_normal':len(test_normal), 'train_neumonia':len(train_neumonia), 'train_normal':len(train_normal)}
per_train=np.round((sets['train_neumonia']+sets['train_normal'])/np.sum(list(sets.values())),4)*100

abs_train = sets['train_neumonia']+sets['train_normal']
abs_test = sets['test_neumonia']+sets['test_normal']
train_neumonia_prop = np.round(sets['train_neumonia']/abs_train,4)*100
test_neumonia_prop = np.round(sets['test_neumonia']/abs_test,4)*100




# Dataset generator:
train_datagen = ImageDataGenerator(rescale = 1/255)
test_datagen = ImageDataGenerator(rescale = 1/255, validation_split = 0.2)

train_generator = ImageDataGenerator(rescale = 1/255,
                                     target_size=(350,350),
                                     batch_size=10,
                                     class_mode='gategorical',
                                     validation_split = 0.2)




# Modelo
model_base = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(350,350,1)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])


#model_base.summary()

model_base.compile(optimizer = 'adam',
                    loss = 'categorical_crossentropy',
                    metrics=['accuracy'])

history = model_base.fit()