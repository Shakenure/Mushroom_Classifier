import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def cat_utility(ds, clustering, m):
  # category utility of clustering of dataset ds
  n = len(ds)  # number items
  d = len(ds[0])  # number attributes/dimensions

  # get number items in each cluster
  cluster_cts = [0] * m  # [0,0]
  for ni in range(n):  # each item
    k = clustering[ni]
    cluster_cts[k] += 1

  for i in range(m): 
    if cluster_cts[i] == 0:   # a cluster has no items
      return 0.0
  # get number unique values, each att
  # ex: [3, 3, 2] -> 3 colors, 3 lengths, 2 weights
  # same as max+1 in ds if ds is encoded
  # used only for list allocation
  unique_vals = [0] * d  # [0,0,0]
  for i in range(d):  # each att/dim
    maxi = 0
    for ni in range(n):  # each item
      if ds[ni][i] > maxi: maxi = ds[ni][i]
    unique_vals[i] = maxi+1

  # get number of each value in each att
  # ex: [[2,1,2], [1,3,1], [2,3]] -- 2 red, 1 blue, etc.
  att_cts = []
  for i in range(d): # each att
    cts = [0] * unique_vals[i] 
    for ni in range(n):  # each data item
      v = ds[ni][i]
      cts[v] += 1
    att_cts.append(cts)

  # get number of each value in each att, each cluster
  # ex: k_cts = [ k=0 [[2,0,0], [1,0,1], [1,1]],  
  #               k=1 [[0,1,2], [0,3,0], [1,2]] ]
  k_cts = []
  for k in range(m):  # each cluster
    a_cts = []
    for i in range(d): # each att
      cts = [0] * unique_vals[i] 
      for ni in range(n):  # each data item
        if clustering[ni] != k: continue  # wrong cluster
        v = ds[ni][i]
        cts[v] += 1
      a_cts.append(cts)
    k_cts.append(a_cts) 

  # uncoditional sum squared probs (right summation)
  un_sum_sq = 0.0 
  for i in range(d):  
    for j in range(len(att_cts[i])):
      un_sum_sq += (1.0 * att_cts[i][j] / n) \
      * (1.0 * att_cts[i][j] / n) 

  # conditional sum, each cluster (left summation)
  cond_sum_sq = [0.0] * m  
  for k in range(m):  # each cluster
    sum = 0.0
    for i in range(d):
      for j in range(len(att_cts[i])):
        if cluster_cts[k] == 0: print("FATAL LOGIC ERROR")
        sum += (1.0 * k_cts[k][i][j] / cluster_cts[k]) \
        * (1.0 * k_cts[k][i][j] / cluster_cts[k])
    cond_sum_sq[k] = sum

  # P(C)
  prob_c = [0.0] * m  # [0.0, 0.0]
  for k in range(m):  # each cluster
    prob_c[k] = (1.0 * cluster_cts[k]) / n  
  # put it all together
  left = 1.0 / m
  right = 0.0
  for k in range(m):
    right += prob_c[k] * (cond_sum_sq[k] - un_sum_sq)
  cu = left * right
  return cu

def cluster(ds, m):
  # ds is encoded
  # greedy algorithm
  n = len(ds)  # number items to cluster
  # assumes first m items are 'different'
  # because they seed the first m clusters
  working_set = [0] * m
  for k in range(m):
    working_set[k] = list(ds[k]) 
    
  clustering = list(range(m))  # [0,1,2, .. m-1]

  for i in range(m, n):
    item_to_cluster = ds[i]
    working_set.append(item_to_cluster)  # working set changed
    
    proposed_clusterings = []  # empty list
    for k in range(m):         # proposed new clusterings
      copy_of_clustering = list(clustering) 
      copy_of_clustering.append(k)
      proposed_clusterings.append(copy_of_clustering) 
    proposed_cus = [0.0] * m   # compute CU of each proposed
    for k in range(m):
      proposed_cus[k] = \
        cat_utility(working_set, proposed_clusterings[k], m)
    # which proposed clustering will give best CU? (greedy)
    best_proposed = np.argmax(proposed_cus)  # 0, 1, . . m-1
    # update clustering
    clustering.append(best_proposed)
  return clustering

# =======================================

def main(a,b,c,d):
  print("\nBegin clustering using category utility demo ")
  raw_data = pd.read_csv('processedMushroomData.csv')  
  X = raw_data.iloc[800:1000,[a,b,c,d]].values 
  
  from sklearn.preprocessing import LabelEncoder
  for i in range(0,4):
      labelencoder_X = LabelEncoder()
      X[:,i]= labelencoder_X.fit_transform(X[:,i])

  m = 2  # number clusters
  print("\nStart clustering with m = %d " % m)
  clustering = cluster(X, m)
  print("Done")

  print("\nResult clustering: ")
  print(clustering) 
  
  ind = np.arange(2)  # the x locations for the groups
  width = 0.7       # the width of the bars
  colors = ['blue','red']
  y = np.bincount(clustering)
  fig, ax = plt.subplots(figsize=(10,7))
  ax.bar(ind, y , width, color=colors)
  #Add some text for labels, title and axes ticks
  ax.set_xlabel("Clusters",fontsize=20)
  ax.set_ylabel('Frequency',fontsize=20)
  ax.set_title('K Means Clustering',fontsize=22)
  ax.set_xticks(ind) #Positioning on the x axis
  #ax.set_xticklabels(('Cluster1', 'Cluster2'),fontsize = 12)
  
  fig.savefig('Resources/chart.png')
  plt.close()

  cu = cat_utility(X, clustering, m)
  print("Category utility of clustering = %0.4f \n" % cu)

  print("\nClustered raw data: ")
  print("=====")
  for k in range(m):
    for i in range(len(X)):
      if clustering[i] == k:
        print(X[i])
    print("====++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++====")
  print("\nEnd demo \n")
