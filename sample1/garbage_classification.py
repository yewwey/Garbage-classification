# -*- coding: utf-8 -*-
"""garbage classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mi9FKuYfz_d6RdwPiXrcRT2NvgwyCSYo
"""

# import numpy as np
# import os

# # 랜덤시드 고정시키기
# np.random.seed(5)
# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# # 데이터셋 불러오기
# train_datagen = ImageDataGenerator(rescale=1./255)
# data_aug_gen = ImageDataGenerator(rescale=1./255, 
#                                   rotation_range=15,
#                                   width_shift_range=0.1,
#                                   height_shift_range=0.1,
#                                   shear_range=0.5,
#                                   zoom_range=[0.8, 2.0],
#                                   horizontal_flip=True,
#                                   vertical_flip=True,
#                                   fill_mode='nearest')
# path = '/content/drive/Shareddrives/예자/Garbage classification/paper/'
# file_list = os.listdir(path)
# for i in file_list:
#     img = load_img('/content/drive/Shareddrives/yeja/Garbage classification/paper/%s'%i)
#     x = img_to_array(img)
#     x = x.reshape((1,) + x.shape)

#     count = 0
# # 이 for는 무한으로 반복되기 때문에 우리가 원하는 반복횟수를 지정하여, 지정된 반복횟수가 되면 빠져나오도록 해야합니다.
#     for batch in data_aug_gen.flow(x, batch_size=1, save_to_dir='/content/drive/Shareddrives/예자/Garbage classification/paper_copy/', save_prefix='tri', save_format='jpg'):
#         count += 1
#         if count > 15:
#             break

# from google.colab import drive
# drive.mount('/content/drive')

from google.colab import drive
drive.mount('/content/drive')

# # 데이터 수 세기
# # cardboard_copy = 4727
# # glass_copy = 5464
# # metal_copy = 4792
# # paper_copy = 6078
# # plastic_copy = 5334
# # trash_copy = 1962
# from imutils import paths

# search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/cardboard_copy"

# image_paths = sorted(
#     list(paths.list_images(search_dir))
# )

# print(">>> image count =", len(image_paths))
# print(image_paths)

import os
import cv2
from tqdm import tqdm
from imutils import paths

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/cardboard_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
image_dim = (150, 150, 3)
labels = []
images = []
for image_path in tqdm(image_paths):
    image = cv2.imread(image_path)

    image = cv2.resize(
        image, (image_dim[1], image_dim[0])
    )
    images.append(image)
    
    label = "cardboard"
    labels.append([label])
    
print(">>> images count =", len(images))

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/glass_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)

for image_path in tqdm(image_paths):
    image = cv2.imread(image_path)

    image = cv2.resize(
        image, (image_dim[1], image_dim[0])
    )
    images.append(image)
    
    label = "glass"
    labels.append([label])
    
print(">>> images count =", len(images))

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/metal_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)

for image_path in tqdm(image_paths):
    image = cv2.imread(image_path)

    image = cv2.resize(
        image, (image_dim[1], image_dim[0])
    )
    images.append(image)
    
    label = "metal"
    labels.append([label])
    
print(">>> images count =", len(images))

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/plastic_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)

for image_path in tqdm(image_paths):
    image = cv2.imread(image_path)

    image = cv2.resize(
        image, (image_dim[1], image_dim[0])
    )
    images.append(image)
    
    label = "plastic"
    labels.append([label])
    
print(">>> images count =", len(images))

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/paper_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)

for image_path in tqdm(image_paths):
    image = cv2.imread(image_path)

    image = cv2.resize(
        image, (image_dim[1], image_dim[0])
    )
    images.append(image)
    
    label = "paper"
    labels.append([label])
    
print(">>> images count =", len(images))

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/trash_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)

for image_path in tqdm(image_paths):
    image = cv2.imread(image_path)

    image = cv2.resize(
        image, (image_dim[1], image_dim[0])
    )
    images.append(image)
    
    label = "trash"
    labels.append([label])
    
print(">>> images count =", len(images))

# import numpy as np
# import os

# # 랜덤시드 고정시키기
# np.random.seed(5)
# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# # 데이터셋 불러오기
# train_datagen = ImageDataGenerator(rescale=1./255)
# data_aug_gen = ImageDataGenerator(rescale=1./255, 
#                                   rotation_range=15,
#                                   width_shift_range=0.1,
#                                   height_shift_range=0.1,
#                                   shear_range=0.5,
#                                   zoom_range=[0.8, 2.0],
#                                   horizontal_flip=True,
#                                   vertical_flip=True,
#                                   fill_mode='nearest')
# path = '/content/drive/Shareddrives/예자/Garbage classification/trash/'
# file_list = os.listdir(path)
# for i in file_list:
#     img = load_img('/content/drive/Shareddrives/yeja/Garbage classification/trash/%s'%i)
#     x = img_to_array(img)
#     x = x.reshape((1,) + x.shape)

#     count = 0
# # 이 for는 무한으로 반복되기 때문에 우리가 원하는 반복횟수를 지정하여, 지정된 반복횟수가 되면 빠져나오도록 해야합니다.
#     for batch in data_aug_gen.flow(x, batch_size=1, save_to_dir='/content/drive/Shareddrives/예자/Garbage classification/trash_copy/', save_prefix='tri', save_format='jpg'):
#         count += 1
#         if count > 14:
#             break
# print("complete")

from imutils import paths

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/glass_copy"

image_paths = sorted(
    list(paths.list_images(search_dir))
)

print(">>> image count =", len(image_paths))
print(image_paths)

import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

images = np.array(images, dtype='float32')/255.0
labels = np.array(labels)

mlb = MultiLabelBinarizer()
enc_labels = mlb.fit_transform(labels)

print(">>> classes name =", mlb.classes_)

x_train = images
y_train = enc_labels

import os
import cv2
from tqdm import tqdm
from imutils import paths

search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/cardboard"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
test_labels = []
test_images = []
for image_path in tqdm(image_paths):
    test_image = cv2.imread(image_path)

    test_image = cv2.resize(
        test_image, (image_dim[1], image_dim[0])
    )
    test_images.append(test_image)
    
    test_label = "cardboard"
    test_labels.append([test_label])
    
print(">>> images count =", len(test_images))
search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/glass"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
for image_path in tqdm(image_paths):
    test_image = cv2.imread(image_path)

    test_image = cv2.resize(
        test_image, (image_dim[1], image_dim[0])
    )
    test_images.append(test_image)
    
    test_label = "glass"
    test_labels.append([test_label])
    
print(">>> images count =", len(test_images))
search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/metal"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
for image_path in tqdm(image_paths):
    test_image = cv2.imread(image_path)

    test_image = cv2.resize(
        test_image, (image_dim[1], image_dim[0])
    )
    test_images.append(test_image)
    
    test_label = "metal"
    test_labels.append([test_label])
    
print(">>> images count =", len(test_images))
search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/paper"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
for image_path in tqdm(image_paths):
    test_image = cv2.imread(image_path)

    test_image = cv2.resize(
        test_image, (image_dim[1], image_dim[0])
    )
    test_images.append(test_image)
    
    test_label = "paper"
    test_labels.append([test_label])
    
print(">>> images count =", len(test_images))
search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/plastic"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
for image_path in tqdm(image_paths):
    test_image = cv2.imread(image_path)

    test_image = cv2.resize(
        test_image, (image_dim[1], image_dim[0])
    )
    test_images.append(test_image)
    
    test_label = "plastic"
    test_labels.append([test_label])
    
print(">>> images count =", len(test_images))
search_dir = "/content/drive/Shareddrives/yeja/Garbage classification/trash"

image_paths = sorted(
    list(paths.list_images(search_dir))
)
for image_path in tqdm(image_paths):
    test_image = cv2.imread(image_path)

    test_image = cv2.resize(
        test_image, (image_dim[1], image_dim[0])
    )
    test_images.append(test_image)
    
    test_label = "trash"
    test_labels.append([test_label])
    
print(">>> images count =", len(test_images))
print(len(test_labels))

import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

test_images = np.array(test_images, dtype='float32')/255.0
test_labels = np.array(test_labels)

mlb = MultiLabelBinarizer()
test_enc_labels = mlb.fit_transform(test_labels)

print(">>> classes name =", mlb.classes_)

seed = 23

(x_test, x_val, y_test, y_val) = train_test_split(
    test_images, test_enc_labels, test_size=0.5, random_state=seed
)
print(">> test test shape = {} {}".format(
    x_test.shape, y_test.shape)
)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.layers import Activation, Flatten, Dropout, Dense

class Classifier:
	def build(width, height, depth, classes):
		model = Sequential()
		input_shape = (height, width, depth)
		
		model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(MaxPooling2D(pool_size=(3, 3)))
		model.add(Dropout(0.25))
  
		model.add(Conv2D(64, (3, 3), padding='same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(Conv2D(64, (3, 3), padding='same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
 
		model.add(Conv2D(128, (3, 3), padding='same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(Conv2D(128, (3, 3), padding='same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
        
		model.add(Conv2D(256, (3, 3), padding='same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(Conv2D(256, (3, 3), padding='same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis=-1))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))

		model.add(Flatten())
		model.add(Dense(2048))
		model.add(Activation('relu'))
		model.add(BatchNormalization())
		model.add(Dropout(0.5))
  
		model.add(Dense(classes))
		model.add(Activation('softmax'))
		return model
        
model = Classifier.build(
    width=image_dim[1], height=image_dim[0], depth=image_dim[2],
    classes=len(mlb.classes_)
)

from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam

batch_size = 16
epoch = 200
learning_rate = 1e-3
decay = learning_rate / epoch

optimizer = Adam(
    learning_rate=learning_rate,
    decay=decay
)

loss = CategoricalCrossentropy(from_logits=False)

model.compile(
    loss=loss,
    optimizer=optimizer,
	metrics=['accuracy']
)

# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# aug = ImageDataGenerator(
#     rotation_range=25, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest'
# )

hist = model.fit(x_train, y_train, epochs=200, batch_size=16, validation_data=(x_val, y_val))

print(hist.history['loss'])
print(hist.history['accuracy'])
print(hist.history['val_loss'])
print(hist.history['val_accuracy'])

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'r', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'g', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'y', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'r', label='train loss')
acc_ax.plot(hist.history['accuracy'], 'b', label='train accuracy')

# val_ax.plot(hist.history['val_loss'], 'r', label='val loss')
# val_ax.plot(hist.history['val_accuracy'], 'b', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

fig, val_loss_ax = plt.subplots()
val_acc_ax = val_loss_ax.twinx()


val_loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
val_acc_ax.plot(hist.history['val_accuracy'], 'b', label='val accuracy')

val_loss_ax.set_xlabel('epoch')
val_loss_ax.set_ylabel('loss')
val_acc_ax.set_ylabel('accuracy')

val_loss_ax.legend(loc='upper left')
val_acc_ax.legend(loc='lower left')

plt.show()

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=16)
print('')
print('loss_and_metrics : ' + str(loss_and_metrics))

from keras.models import load_model
model.save('/content/drive/Shareddrives/yeja/Garbage classification/garbage_classification_model.h5')

pip install graphviz

pip install pydot

model.summary()

from tensorflow.keras.utils import plot_model

plot_model(model, to_file='/content/drive/Shareddrives/yeja/Garbage classification/model_architecture.png')
plot_model(model, to_file='/content/drive/Shareddrives/yeja/Garbage classification/model_shapes.png', show_shapes=True)

# hist = model.fit(
# 	aug.flow(
#         x_train, y_train, batch_size=batch_size
#     ),
# 	validation_data=(x_test, y_test),
# 	steps_per_epoch=len(x_train) // batch_size,
# 	epochs=epoch, verbose=1
# ).history

# steps_per_epoch = train_size // BATCH_SIZE
# validation_steps = valid_size // BATCH_SIZE
# hist = model.fit(
#     train_ds,
#     epochs=5, steps_per_epoch=steps_per_epoch,
#     validation_data=val_ds,
#     validation_steps=validation_steps).history