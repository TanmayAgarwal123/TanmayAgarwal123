# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import warnings

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split  


warnings.simplefilter(action='ignore', category=FutureWarning)

# reading csv file and extracting class column to y.
dataf = pd.read_csv("Datasetinfectedhealthy.csv").fillna(0)

# extracting two features
X = dataf.drop(['imgid','fold num'], axis=1)
y = X['label']
X = X.drop('label', axis=1)

print("\nTraining dataset:-\n")
print(X)


#preparing test dataset
log = pd.read_csv("Datasetunlabelledlog.csv")

log = log.tail(1)
X_ul = log.drop(['imgid','fold num'], axis=1)

print("\nTest dataset:-\n")
print(X_ul)

#splitting dataset into training and testing

x_train, Xi_test, y_train, yi_test = train_test_split(X, y, test_size=0.32, random_state=60,shuffle=True)  
        # here take care of the train test split size and shuffling, show them incorrect parametes will lead to incorrect results
#creating instance variable for SVM Classifier
svclassifier = SVC(kernel='linear') 
#training the model 
svclassifier.fit(x_train, y_train)  
#predicting the test dataset
pred = svclassifier.predict(X_ul)

print("\nprediction: %d" %int(pred))

#if prediction <0.5 then infected else healthy
if(pred < 0.5):
	print("The leaf is sufficiently healthy!")
else:
	print("The leaf is infected!")

print("\nKeypress esc on any image window to terminate")

cv2.waitKey(0)
