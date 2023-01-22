#importing numpy
import numpy as np

if __name__ == '__main__':
    #creating an array using np.ogrid
    i, j = np.ogrid[:3, :3]

    #For question 1, use np.where to create a conditional statement in the format (condition, if so then, else)
    Q1 = np.where(i == j, 1 , 0)
    print (Q1, "\n")

    #For quesion 2, use the np.where condition to add 3 to each cell where i does not equal j
    Q2 = np.where(i != j, Q1 + 3 , Q1 + 0)
    print (Q2, "\n")

    #For question 3, use np.delete to delte the last column of Q2
    Q3 = np.delete(Q2,-1,1)
    print (Q3, "\n")




























