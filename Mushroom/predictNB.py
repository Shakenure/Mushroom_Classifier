import pickle
from .trainNaiveBayes import edibleProb, poisonousProb

import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render


#get conditional probability
#prob: type of probability
#attribute: column type
#attrType: type of attribute
def getP(freq, prob, attribute, attrType):
    #return freq[attribute][prob][attrType]
    return float(freq[attribute][prob].where(freq[attribute][attribute] == attrType).dropna())


#get edibility
#input: prob values for E and P
def edibility(e, p):
    if(e > p):
        return 'Edible'
    else:
        return 'Poisonous'


def calcProbFactor(inputValues):
    # Load data (deserialize)
    with open('probTable.pickle', 'rb') as handle:
        freq = pickle.load(handle)

    E = edibleProb()
    P = poisonousProb()
    edible = []
    poisonous = []
    response = str(E)+" "+str(P)+"<br>"
    for attr, attrType in inputValues.items():
        E = E*getP(freq, 'P_X_Edible', attr, attrType)/getP(freq, 'P_X', attr, attrType)
        P = P*getP(freq, 'P_X_Poisonous', attr, attrType)/getP(freq, 'P_X', attr, attrType)
        edible.append(E)
        poisonous.append(P)
        response += str(E)+" "+str(P)+"<br>"
    print(edible)
    print(poisonous)

    

    
    return edible, poisonous, "<h1>"+edibility(E, P)+"</h1>"
    