import numpy as np
import pandas as pd
# you can import your favorite libraries here, as long as they run on SL2 machines

# Task 1
## create an nXn INTEGER matrix and store it with checkerboard pattern (using 0's and 1's). Top left corner should be 0. No loops. Assume n > 0.
def checkerboard(n):
    x = np.zeros((n, n), dtype = int)
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
    return x
    pass

# Task 2
def SimpleNonLinearity(arr, leak):
    arrcpy=arr.copy()
    arrcpy=arrcpy.astype('float')
    req = arrcpy<=0
    arrcpy[req]=arrcpy[req]*leak
    return arrcpy
    pass

# Task 3
## write a function to normalise an array of shape (m, n) along its columns. By normalise, we mean that mean of each column should be 0 and variance of each column is 1.
def normalise(arr):
    # compute mean (along columns) and reshape it into a row vector
    # then subtract this from each row of arr (let's call it mean_normalised)
    # then compute the std. deviation of the mean_normalised and reshape it into a row vector.
    # divide each row of mean_normalised by std.dev. to get the result.
    # write your code here
    me=arr.mean(axis=0)
    normalised_me=arr - me
    sigma=normalised_me.std(axis=0)
    return normalised_me/sigma
    pass

# Task 4
"""
write a function to get the positions of top_k values of an each row of a matrix of shape (m,n).

Concretely, if A is the input matrix of shape (m,n), then return an integer matrix R, such that:
R_{ij} is the index of an element in ith row of A which has rank j when that row is sorted in decreasing order. 
For example, if the input array ‘arr’ is:
[[ 6  4  4  7]
 [ 7  8  1  0]
 [11 10  5 11]]
Then top_k(arr, 2) will be:
[[3 0]
 [1 0]
 [3 0]]
Explanation for first row:
when we sort 6,4,4,7 in decreasing order, we get:
7, 6, 4, 4. Top 2 elements are 7 and 6. And, their positions in arr are: 3 and 0 respectively. 
So, the first row of result is 3,0.

Note: for breaking ties, higher indices should come first.(See the last row of result).
"""
def top_k(mat, k):
    result=np.argsort(mat)
    result=np.flip(result,axis=1)
    result=result[:,range(k)]
    return result
    pass

# Task 5
## write a function which takes an array of shape (n,n) and returns either True or False, depending on whether the input was a magic square or not.
def is_magic_square(square):
    n=square.shape[0]
    p = square.trace()
    q = np.flip(square,axis=1).trace()
    r = square.sum(axis=1)
    s = square.sum(axis=0)
    check1 = (n*n == len(np.unique(square)))
    check2 = (p==q)
    check3 = (r==q).all()
    check4 = (s==q).all()
    return check1 and check2 and check3 and check4
    pass
