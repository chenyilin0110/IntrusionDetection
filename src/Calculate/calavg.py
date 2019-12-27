import numpy as np
import sys

run = sys.argv[1]
folder = sys.argv[2]
file_name = sys.argv[3]
data = np.loadtxt('src/' + folder + '/result/' + file_name + '.txt', delimiter='\n')
avg_list = []

count = 0
for i in range(len(data)):
    count += data[i]
print(count/int(run))