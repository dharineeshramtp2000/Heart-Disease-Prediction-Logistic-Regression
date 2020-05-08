import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dataset = pd.read_csv("heart_disease_dataset.csv")
X = Dataset.iloc[:, :-1].values
y = Dataset.iloc[:, -1].values

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state=42, shuffle=True)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(max_iter=1000, random_state = 0, multi_class='ovr', solver='lbfgs')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
acc_train = accuracy_score(y_train, classifier.predict(X_train))
f1_train = f1_score(y_train, classifier.predict(X_train), average= 'weighted')

print("Traing set results")
print("ACCURACY ---------------------->",acc_train)
print("F1 SCORE ---------------------->",f1_train)

#Now lets see how well is our model. So now lets evaluate with our test set
acc_test = accuracy_score(y_test, y_pred)
f1_test = f1_score(y_test, y_pred, average= 'weighted')

print("Test set results")
print("ACCURACY ---------------------->",acc_test)
print("F1 SCORE ---------------------->",f1_test)

#Now lets have our famous Confusion Matrix to visually understand.
cm = confusion_matrix(y_test,y_pred)
print(cm)

