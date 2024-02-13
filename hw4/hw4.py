import csv
import numpy as np
from numpy import std, mean
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def load_data(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        ans = []
        for line in reader:
            ans.append(line)
        return(ans)
    
def calc_features(row):
    ans = []
    for i,j in row.items():
        if i == "" or i == "Country":
            continue
        else:
            ans.append(float(j))
    np.reshape(ans, (6,))
    ans = np.array(ans).astype("float64")
    return ans

def hac(features):
    #length(features)
    lenf = len(features)

    #the answer -> len(features)-1(num of paths), 4(we have to find 4 z)
    ans = np.zeros((lenf-1, 4))

    #Number each of your starting data points from 0 to n − 1
    numCon = {}
    for i in range(lenf):
        #value is the number of countries (처음에는 모두 1로 시작)
        numCon[i] = 1

    #find distance between two clusters
    distance = np.zeros((lenf, lenf))
    for i in range(lenf):
        for j in range(lenf):
            distance[i, j] = np.linalg.norm(features[i] - features[j])

    
    #find Z[i, 0], Z[i, 1], Z[i, 2], Z[i, 3] and put them into cList
    #path is length of features - 1 
    for i in range(lenf-1):
        #base case
        if len(numCon) <= 1:
            break

        #otherwise find the cloest distance between the clusters
        minDistance = np.inf #np.inf means positive infinity
        z0, z1 = 0, 0
        #numCon is a dictionary, thus we will use the key of the dictionary
        for first in numCon.keys():
            for second in numCon.keys():
                #distance cannot be 0 -> 0 means cluster itself
                if distance[first, second] != 0:
                    #if new value is lower than the minimum distance
                    if distance[int(first), int(second)] < minDistance:
                        z0, z1 = first, second
                        #initialize min distance to new distance
                        minDistance = distance[int(first), int(second)]

        #new cluster
        newC = []
        for c in range(lenf + i):
            #append the new cluster and the other clusters' max distance (complete-linkage)
            newC = np.append(newC, max(distance[z0, c], distance[z1, c]))
        #vstack -> stands for vertical stack [[1,2],[3,4]]
        distance = np.vstack((distance, newC))
        #0 is for distance of new cluster itself
        newC = np.append(newC, 0)
        newC = np.reshape(newC, (lenf + i + 1, 1))
        #hstack -> stands for horizontal stack [[1,2,3,4]]
        distance = np.hstack((distance, newC))
  
        # Z[i, 0] first element
        # Z[i, 1] second element  
        ans[i][0] = float(z0)
        ans[i][1] = float(z1)

        # Z[i, 2] distance between the two clusters 
        ans[i][2] = float(distance[int(z0), int(z1)])
        # Z[i, 3] total number of countries
        z3 = numCon.pop(z0) + numCon.pop(z1)
        ans[i][3] = float(z3)
        numCon[lenf + i] = z3
    return ans

def fig_hac(Z, names):
    fig = plt.figure()
    dendrogram(Z, labels=names, leaf_rotation = 90)
    fig.tight_layout()
    return fig

def normalize_features(features):
    ans = []
    means = mean(features, axis=0)
    stds = std(features, axis=0)
    normalizeF = ((features- means)/stds)
    for i in normalizeF:
        ans.append(i)
    return ans