import numpy as np
import sys

run = sys.argv[1]
algorithm = sys.argv[2]
dataset = sys.argv[3]
file_name = sys.argv[4]
data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + file_name + '.txt', delimiter='\n')

avg_list = []

count = 0
for i in range(len(data)):
    count += data[i]
print(count/int(run), end=' ')