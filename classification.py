import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

#Importing the csv file containing the kmer features for each sequence
df = pd.read_csv("data_with_2kmer_features.csv")

#Dropping the 'Sequence ID' and 'Nucleotide Sequence' columns as they are not necessary for classification
df = df.drop(['Sequence ID', 'Nucleotide Sequence'], axis=1)

#Set the parameters for cv and save to variable kf
kf = KFold(n_splits=5, shuffle=True, random_state=25)

#Saving the labels for each sequence as 'y'
y = df["Label"]

#Saving the features for each sequence as 'x'
x = df.iloc[0:df.shape[0],1:df.shape[1]]

#Using 5-fold cross validation to assess the performance of using the Random Forest algo to build a classifier model using different parts of the data
for training_index, test_index in kf.split(df):
    #Splitting the data into training and testing sets for each iteration of CV
    x_train, x_test = x.iloc[training_index], x.iloc[test_index]
    y_train, y_test = y.iloc[training_index], y.iloc[test_index]

    #Creating a RF Classifier object
    RF_classifier = RandomForestClassifier(random_state=0)

    #Training a random forest model using the training data
    RF_classifier.fit(x_train, y_train)

    #Prediciting the class for the test set
    y_pred = RF_classifier.predict(x_test)

    #Assessing the performance of the model
    print("Accuracy of the model:", metrics.accuracy_score(y_test, y_pred))
    print(metrics.confusion_matrix(y_test,y_pred))