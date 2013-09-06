import numpy as np, sys

#allows you to read in a file into a variable
file_in = open(sys.argv[1], 'r')

#loads strings into a numpy array
a = np.loadtxt(file_in, delimiter=' ', unpack=True)

#selects the second dimenstion of the array
x = a[:,1]
total = sum(x)
print sys.argv[1], total
