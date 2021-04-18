# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:58:25 2021

@author: mteg_label3
"""

import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dropout, Dense
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


#load data
fidr=r'C:\Users\mteg_label3\Desktop\python\digit-recognizer\\'
train=pd.read_csv(fidr+'train.csv')
test=pd.read_csv(fidr+'test.csv')

#generate x,y
y_train=train["label"]
x_train=train.drop(labels="label",axis=1)

#nomailization
x_train=x_train/255
test=test/255

#reshpae
x_train=x_train.values.reshape(-1,28,28,1)
test=test.values.reshape(-1,28,28,1)

#one hot encoding y
y_train=to_categorical(y_train, num_classes=10)

#train, test split
x_train, x_val, y_train, y_val=train_test_split(x_train, y_train, 
                                                test_size=0.1, random_state=2)

#CNN model
model=Sequential()
model.add(Conv2D(filters=64, kernel_size=(5,5), padding='same', 
                 activation='relu', input_shape=(28,28,1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.5))
model.add(Conv2D(filters=128, kernel_size=(5,5), padding='same', 
                 activation='relu', input_shape=(28,28,1)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
model.summary()

#compile the model
model.compile(optimizer='Adam',loss="categorical_crossentropy",metrics="acc")

#ImageDataGenerator
datagen =ImageDataGenerator(
        featurewise_center=False,
        samplewise_center=False,
        featurewise_std_normalization=False,
        samplewise_std_normalization=False,
        zca_whitening=False,
        rotation_range=10,
        zoom_range=0.2,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=False,
        vertical_flip=False)

datagen.fit(x_train)

#fit the model
history=model.fit_generator(datagen.flow(x_train,y_train, batch_size=64),
                            epochs=3, verbose=2, validation_data=(x_val,y_val),
                            steps_per_epoch=x_train.shape[0]//64)

#loss, acc curves
fig,ax=plt.subplots(2,1)
ax[0].plot(history.history["loss"], color='b', label="Training loss")
ax[0].plot(history.history["val_loss"], color='r', label="Validation loss",axes =ax[0])
legend=ax[0].legend(loc="best", shadow=True)

ax[1].plot(history.history["acc"], color='b', label="Training acc")
ax[1].plot(history.history["val_acc"], color='r', label="Validation acc")
legend=ax[1].legend(loc="best", shadow=True)

#confusion maxtrix
y_pred=model.predict(x_val)
y_pred_classes=np.argmax(y_pred,axis=1)
y_true=np.argmax(y_val,axis=1)
confusion_mtx=confusion_matrix(y_true, y_pred_classes)
f, ax=plt.subplots(figsize=(7,7))
sns.heatmap(confusion_mtx,annot=True, linewidths=0.01, cmap="Blues", linecolor="gray", fmt=".1f",ax=ax)
#plt.xlabel("Predicted Label")
#plt.ylabel("True Label")
#plt.tilte("Confusion Matrix")
plt.show()

# predict results
results = model.predict(test)

# select the indix with the maximum probability
results = np.argmax(results,axis = 1)
results = pd.Series(results,name="Label")
submission = pd.concat([pd.Series(range(1,28001),name = "ImageId"),results],axis = 1)
submission.to_csv("predicted test.csv",index=False)