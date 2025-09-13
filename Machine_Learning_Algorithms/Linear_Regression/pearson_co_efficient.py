#Calculate pearson co-efficient between two variables

from numpy.random import randn,seed
from scipy.stats import pearsonr

seed(1)

#Data Preparation
data1 = 20 * randn(1000) + 50
data2 = data1 + (10 * randn(1000) + 100)

#Pearson-coefficient
corr, p = pearsonr(data1,data2)

print("Pearson Co-efficient %.3f"%corr)

if p > 0.5:
    print("No co-relation to reject null hypothesis")
else:
    print("Some co-relation to reject null hypothesis")


### SUMMARY 

# The Pearsons correlation coefecient can be used to evaluate the relationship between more than two variables. 

# This can be done by calculating a matrix of the relationships between each pair of variables in the dataset. 

# The result is a symmetric matrix called a correlation matrix with a value of 1.0 along the diagonal as each column always perfectly correlates with itself.
