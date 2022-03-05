import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import joblib

data = pd.read_csv('train.csv')
#Create one hot encoder object
ohe = OneHotEncoder()

#delete some columns of data that don't matter to us

data = data.drop(['Embarked'], axis=1)
data = data.drop(['PassengerId'], axis=1)
data = data.drop(['Cabin'], axis=1)
data = data.drop(['Ticket'], axis=1)
data = data.drop(['Name'], axis=1)

# check for missing Age instances in data
pop=data['Age'].isnull()
# delete the entire row (passenger) if age is missing
data = data[~pop]


x = data.iloc[:, :].values
array = ohe.fit_transform(x[:, 1:3]).toarray()
categ = ohe.categories_
#one hot encoding creates dummy variables
dummy = pd.DataFrame(array)
# print(categ)
data_x = pd.DataFrame(x)
# target data is the survive or not column
y = data_x[0]
y = y.astype('int')
data_x = data_x.drop([0, 1, 2], axis=1)
# concatenate the dummy variables with the rest of the data
data_x = pd.concat([dummy, data_x], axis=1)
# print(data_x.tail())

# split the data into test and train
x_train, x_test, y_train, y_test = train_test_split(data_x, y, test_size=0.20, random_state=101)
# create RandomForestClassifier object
rf_model = RandomForestClassifier()

#train the model to fit the train data
rf_model.fit(x_train, y_train)

# print the scores if you want
# print(rf_model.score(x_test,y_test))
# print(rf_model.score(x_train, y_train))

# Finally, sava the model to use later
filename = 'finalized_model.sav'
joblib.dump(rf_model, filename)



