# EXERCICE 2

#
# Question 1
#

# 

#
#  Question 2
#


def LSUBSTRREC(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0
    elif X[len(X) - 1] == Y[len(Y) - 1]:
        return LSUBSTRREC(X[:len(X) - 1], Y[:len(Y) - 1]) + 1
    else:
        return max(LSUBSTRREC(X, Y[:len(Y) - 1]), LSUBSTRREC(X[:len(X) - 1], Y))

def LSUBSTR(X, Y):
    L = [[None] * (len(Y) + 1) for i in range(len(X) + 1)]

    for i in range(len(X) + 1):
        for j in range(len(Y) + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[len(X)][len(Y)]

#
#   Question 3
#

import numpy as np

def LSUBSTR_DYN(X, Y):
    
    L = np.zeros((len(X), len(Y)))
    max = 0
    indice_max = 0
    
    for i in range(len(X)):
        for j in range(len(Y)):
            
            if X[i] == Y[j]:
                
                if i == 0 or j == 0:
                    L[i, j] = 1
                else:
                    L[i, j] = L[i-1,j-1] + 1
                    
                if L[i, j] > max:
                    max = int(L[i,j])
                    indice_max = i

    return X[indice_max + 1 - max:indice_max + 1]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(LSUBSTR(X, Y))
    print(LSUBSTR_DYN('navire','coronavirus'))
