#Read Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import sklearn.model_selection as model_selection
pd.options.display.max_rows = 100

#Read in data
data=pd.read_csv(r'\\pokemon.csv')
df = pd.DataFrame(data)
#Remove exteraneous columns
df.drop(df.columns[0], axis=1,inplace = True)
df.head()


#Convert Legendary into boolean, remove index feature
df.loc[df['Legendary']==False,'Legendary'] = 0
df.loc[df['Legendary']==True,'Legendary'] = 1
df.drop(df.columns[0], axis=1,inplace = True)


#If the Pokemon only has one Type, fill the NA with the Type1 value
df.loc[df['Type 2'].isnull(),'Type 2'] = df.loc[df['Type 2'].isnull(),'Type 1']

#Convert both Type values to numeric categorical features
df['Type 1'] = df['Type 1'].astype('category')
df['Type 1'] = df['Type 1'].cat.codes + 1
df['Type 2'] = df['Type 2'].astype('category')
df['Type 2'] = df['Type 2'].cat.codes + 1


#Select the numeric columns and generate descriptive statistics about them
num_df = df.drop(df.columns[[0,1,9,10]], axis=1)
num_df.describe()


#Removing high leverage points based on exploratory analysis
df.loc[df['Sp. Def']>=150, 'Sp. Def'] = np.mean(df['Sp. Def'])
df.loc[df['Sp. Def']<=10, 'Sp. Def'] = np.mean(df['Sp. Def'])
df.loc[df['Defense']>=150, 'Defense'] = np.mean(df['Defense'])
df.loc[df['Defense']<=25, 'Defense'] = np.mean(df['Defense'])
df.loc[df['Speed']>=150, 'Speed'] = np.mean(df['Speed'])
df.loc[df['HP']>=150, 'HP'] = np.mean(df['HP'])


#Side-by-side seaborn scatterplots of three of the features plotted against the total
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharey=True,figsize=(14,5))
sns.scatterplot(data=df,x="HP",y="Total",ax=ax1)
sns.scatterplot(data=df,x="Defense",y="Total",ax=ax2)
sns.scatterplot(data=df,x="Sp. Def",y="Total",ax=ax3)

#Side-by-side seaborn scatterplots of another three features plotted against the total
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharey=True,figsize=(14,5))
sns.scatterplot(data=df,x="Attack",y="Total",ax=ax1)
sns.scatterplot(data=df,x="Sp. Atk",y="Total",ax=ax2)
sns.scatterplot(data=df,x="Speed",y="Total",ax=ax3)


#Creation of a dummy feature to teach data transformations with, application of a log transformation
df['Test']=df['Speed']
df['Test'] = np.log(df['Test'])
sns.scatterplot(data=df,x="Test",y="Total")


#Nth (Cubed) root transformation on the test dummy variable
df['Test'] = df['Test']**(1./3.)
sns.scatterplot(data=df,x="Test",y="Total")


#Inverse transformation with subsequent high leverage point removal on the test dummy variable
df['Test'] =  1/df['Test']
df.loc[df['Test']>=0.75, 'Test'] = np.mean(df['Test'])
sns.scatterplot(data=df,x="Test",y="Total")


#Exponential transformation on the test dummy variable
df['Test'] = df['Test'] * 1000
sns.scatterplot(data=df,x="Test",y="Total")



#Feature engineering practice re-producing the Total column from the other features and comparing against existing Total
df['Total2'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
(df['Total'] == df['Total2']).sum()
#Removal of all engineered columns + multicollinear total column
df.drop(['Test','Total','Total2'], axis=1, inplace=True)


#Separate Xs and y into different structures, split into train and test sets
X=df.drop('Legendary', axis=1)
y=df["Legendary"]
y=y.astype('int')
Xval_train, Xval_test, yval_train, yval_test = model_selection.train_test_split(X,y,test_size=0.2, random_state=136)


#Examine distribution of legendary/non-legendary values in y train and test sets
yval_train.value_counts()
yval_test.value_counts()


#Model Data
model = SVC(kernel='linear')
model.fit(Xval_train, yval_train)
#Apply model to test set
svm_fitted = model.predict(Xval_test)


#Plot truth table
matrx = confusion_matrix(yval_test, svm_fitted)
sns.heatmap(matrx.T, square=True, annot=True, fmt='d',cbar=False,cmap="bone_r")
plt.xlabel('True')
plt.ylabel('Prediction')


#Plot ROC curve
fpr, tpr, _ = roc_curve(yval_test, svm_fitted)
auc = roc_auc_score(yval_test, svm_fitted)
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()