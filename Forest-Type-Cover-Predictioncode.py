# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here

# read the dataset
dataset = pd.read_csv(path)

# look at the first five columns
print(dataset.head())

# Check if there's any column which is not useful and remove it like the column id
dataset = dataset.drop('Id',1)
print(dataset.info())

# check the statistical description
print(dataset.describe())


# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols = dataset.columns

#number of attributes (exclude target)
size = cols.size - 1
print(size)
#x-axis has target attribute to distinguish between classes
x = dataset.Cover_Type
#y-axis shows values of an attribute
y = dataset.drop('Cover_Type',1)

#Plot violin for all attributes
for i in range(1,size):
   sns.violinplot(x = 'Cover_Type', y = cols[i], data = dataset)


# --------------
import seaborn as sns
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here
subset_train = dataset.iloc[:,0:10]

data_corr = subset_train.corr()

sns.heatmap(data_corr,annot = True)

correlation  = data_corr.unstack().sort_values(kind ='quicksort')
print(type(correlation))
corr_var_list = correlation.loc[((correlation  > upper_threshold) | (correlation < lower_threshold)) & (correlation!=1)]
print(corr_var_list)

# Code ends here




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)

X = dataset.drop('Cover_Type',1)
Y = dataset.Cover_Type

X_train,X_test,Y_train,Y_test = cross_validation.train_test_split(X,Y,test_size = 0.2,random_state = 0)

# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.

scaler =  StandardScaler()

X_train_temp = scaler.fit_transform(X_train.iloc[:,0:10])

#Standardized
#Apply transform only for continuous data
X_test_temp = scaler.transform(X_test.iloc[:,0:10])

#Concatenate scaled continuous data and categorical
X_train_1 = np.concatenate((X_train_temp,X_train.iloc[:,10:]),axis = 1)

X_test_1 = np.concatenate((X_test_temp,X_test.iloc[:,10:]),axis = 1)

scaled_features_train_df = pd.DataFrame(data = X_train_1, index = X_train.index, columns = X_train.columns)

scaled_features_test_df =  pd.DataFrame(data = X_test_1, index = X_test.index, columns = X_test.columns)





# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:
skb = SelectPercentile(score_func = f_classif, percentile = 90)

predictors = skb.fit_transform(X_train_1,Y_train)

scores = skb.scores_

Features = scaled_features_train_df.columns

dataframe = pd.DataFrame({'Features' : Features, 'Scores' : scores})

dataframe = dataframe.sort_values(by ='Scores', ascending =False)

top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])

print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score

clf = LogisticRegression()

clf1 = OneVsRestClassifier(clf)

model_fit_all_features = clf1.fit(X_train,Y_train)

predictions_all_features = clf1.predict(X_test)

score_all_features = accuracy_score(Y_test,predictions_all_features)

model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors],Y_train)

predictions_top_features = clf.predict(scaled_features_test_df[top_k_predictors])

score_top_features = accuracy_score(Y_test,predictions_top_features)

print('score_top_features',score_top_features)
print('score_all_features',score_all_features)


