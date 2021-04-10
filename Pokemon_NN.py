#Read Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sklearn.model_selection as model_selection
pd.options.display.max_rows = 100

#New NN Packages
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Dropout

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



#Plot histogram of "Attack" feature's distribution
x=df['Attack']
plt.hist(x, bins = 8)
plt.show()


#Plot bar chart showing Type 1 values against the Total
plt.bar(df['Type 1'],df['Total'],width=0.5)
plt.xticks(df['Type 1'], rotation='vertical')
plt.show()


#Plot a pie chart of the Type 1 values by size of aggregate Total values
df.groupby(['Type 1']).sum().plot(kind='pie', y='Total',legend=False)


#Plot a bubble chart of Attack against Total, Pokemon with higher Special Attack represented larger, and a color distinction for Legendaries
sns.scatterplot(data=df, x="Attack", y="Total", size="Sp. Atk", hue="Legendary",legend=False, sizes=(2, 500))


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



#Convert both Type values to numeric categorical features
df['Type 1'] = df['Type 1'].astype('category')
df['Type 1'] = df['Type 1'].cat.codes + 1
df['Type 2'] = df['Type 2'].astype('category')
df['Type 2'] = df['Type 2'].cat.codes + 1


#Feature engineering practice re-producing the Total column from the other features and comparing against existing Total
df['Total2'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
(df['Total'] == df['Total2']).sum()
#Removal of all engineered columns + multicollinear total column
df.drop(['Test','Total','Total2'], axis=1, inplace=True)


#Convert X to a float array, split train and test
X=df.drop('Legendary', axis=1)
y=df["Legendary"]
y=y.astype('int')
X = np.array(X, dtype=np.float32)
Xval_train, Xval_test, yval_train, yval_test = model_selection.train_test_split(X,y,test_size=0.2, random_state=136)


#Initialize Sequential Model
model = keras.Sequential([
    Dense(150, activation=tf.nn.relu),
    Dense(75, activation='sigmoid'),
    Dropout(0.2),
    Dense(1,activation='sigmoid')
])


#Fit Model
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])
model.fit(x=Xval_train,y=yval_train, epochs=10)

      
#Predict with New Data    
nn_fitted = model.predict(Xval_test)