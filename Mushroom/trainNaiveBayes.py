import pandas as pd
import pickle

df = pd.read_csv('processedMushroomData.csv')

train=df.sample(frac=0.8,random_state=200) #random state is a seed value
X = train.iloc[:, 1:]
Y = train.iloc[:, 0]
test=df.drop(train.index)


total = train['Edibility'].count()
e = train[train['Edibility'] == 'edible']['Edibility'].count()
p = train[train['Edibility'] == 'poisonous']['Edibility'].count()

#class probabilities
def edibleProb():
    return e/total

def poisonousProb():
    return p/total

P_Edible = edibleProb()
P_Poisonous = poisonousProb()

#conditional probability
def conditional_Prob(str):
    freq = train.groupby(train[str]).size().reset_index(name = 'Count')
    
    freq['P_X'] = freq['Count']/total
    
    freq['P_X_Edible'] = freq[str].apply(
            lambda x: train[(train[str] == x) & (train['Edibility'] == 'edible')]['Edibility'].count()/e
            )
    freq['P_X_Poisonous'] = freq[str].apply(
            lambda x: train[(train[str] == x) & (train['Edibility'] == 'poisonous')]['Edibility'].count()/p
        )
    
    noOfTypes = freq['P_X_Edible'].count()
    if freq['P_X_Edible'].eq(0).any():
        #laplaceSmoothing
        freq['P_X_Edible'] = freq[str].apply(
            lambda x: (train[(train[str] == x) & (train['Edibility'] == 'edible')]['Edibility'].count()+1)/(e+noOfTypes)
            )

    if freq['P_X_Poisonous'].eq(0).any(): 
        freq['P_X_Poisonous'] = freq[str].apply(
            lambda x: (train[(train[str] == x) & (train['Edibility'] == 'poisonous')]['Edibility'].count()+1)/(p+noOfTypes)
            )
    
    freq['P_Edible_X'] = freq['P_X_Edible']*P_Edible/freq['P_X']
    freq['P_Poisonous_X'] = freq['P_X_Poisonous']*P_Poisonous/freq['P_X']
    
    return freq


#model
freq = {}
for col in X.columns:
    freq[col] = conditional_Prob(col)

    
with open('probTable.pickle', 'wb') as handle:
    pickle.dump(freq, handle, protocol=pickle.HIGHEST_PROTOCOL)