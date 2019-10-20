import numpy as np
import sys

finder = sys.argv[1]
filename = sys.argv[2]
run = sys.argv[3]

dataset = np.loadtxt(finder+'/'+filename, dtype=np.str, delimiter=' ')
temp = dataset[:].astype(float)

accuracy = np.zeros(int(run))

total = 0
for i in range(len(temp)):
    total += temp[i]
total = total/int(run)
print(total)