import pandas as pd
import sys
from matplotlib import pyplot as plt
import numpy as np

def load_data(filename):
    with open(filename, 'r') as f:
        reader = pd.read_csv(f)
    return reader

def visualize(data):
    plt.plot(data.year, data.days)
    plt.xticks([t for t in data.year])
    plt.xlabel("Year")
    plt.ylabel("Number of Frozen Days")
    plt.savefig("plot.jpg") # must be plot.jpg

def q3a(data):
    #make X as an array
    X = []
    #x <- year of the dataset
    for i in data.year:
        #transpose all the data and append in X
        transpose = np.transpose([1,i])
        X.append(transpose)
    #reshape it to dimension n × 2 ([1,xi])
    X = np.reshape(X, (len(X), 2))
    #make sure data type is int64
    X = np.array(X).astype("int64")
    return X

def q3b(data):
    #make Y as an array
    Y = []
    for i in data.days:
        #append all the days in Y
        Y.append(i)
    Y = np.reshape(Y, (len(Y)))
    #make sure data type is int64
    Y = np.array(Y).astype("int64")
    return Y

def q3c(X):
    #Z = X^T * X
    Z = np.transpose(X).dot(X)
    Z = np.array(Z).astype("int64")
    return Z

def q3d(X):
    #inverse the data of Z
    I = np.linalg.inv(q3c(X))
    return I

def q3e(X): 
    #PI = (X^T * X)^(-1) * X^T
    PI = q3d(X).dot(np.transpose(X))
    return PI

def q3f(X, Y):
    #β = (X^T * X)^(-1) * X^T * Y
    b = q3e(X).dot(Y)
    return b

def prediction(b):
    testY = b[0] + b[1] * 2022
    return testY

def interpretation(b):
    #if b1 = 0 -> =
    if b[1] == 0:
        return '='
    #if b[1] > 0 -> >
    elif b[1] > 0:
        return '>'
    #if b[1] < 0 -> <
    elif b[1] < 0:
        return '<'
    
def limitation(b):
    #0 = b0 +b1 * x(noFreeze)
    #-bo = b1 * x(noFreeze)
    #-(bo / b1) = x(noFreeze)
    noFreeze = -(b[0]/b[1])
    return noFreeze

if __name__=="__main__":
    #Q2
    filename = sys.argv[1] # the first argument as string
    try:
        data = load_data(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)
    
    #for Q2 graph
    visualize(data)

    #Q3a
    X = q3a(data)
    print("Q3a:")
    print(X) # Your X.dtype needs to be int64

    #Q3b
    Y = q3b(data)
    print("Q3b:")
    print(Y) # Your Y.dtype needs to be int64

    #Q3c
    Z = q3c(X)
    print("Q3c:")
    print(Z) # Your Z.dtype needs to be int64

    #Q3d
    I = q3d(X)
    print("Q3d:")
    print(I)

    #Q3e
    PI = q3e(X)
    print("Q3e:")
    print(PI)

    #Q3f
    b = q3f(X, Y)
    print("Q3f:")
    print(b)

    #Q4
    testY = prediction(b)
    print("Q4: " + str(testY))

    #Q5
    ##(a)
    interpretation = interpretation(b)
    print("Q5a: " + str(interpretation))

    ##(b)
    print("Q5b: " + "")

    #Q6
    ##(a)
    limitation = limitation(b)
    print("Q6a: " + str(limitation))

    ##(b)
    print("Q6b: " + "")
