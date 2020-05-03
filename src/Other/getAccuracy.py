import numpy as np
import sys

algorithm = sys.argv[1]
dataset = sys.argv[2]
datasetNumber = sys.argv[3]
categories = sys.argv[4]
run = sys.argv[5]

# copy acc to other file 
for i in range(int(datasetNumber)):
    f = open('src/' + algorithm +'_' + dataset + '/result/' + 'experimental_result_' + categories + '-' + str(i+1) + '.txt', "a")
    for j in range(int(run)):
        data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'experimental_result_' + categories + '-' + str((i+1)) + '-' + str(j+1) + '.txt', delimiter='\n')
        f.write(str(data[-1]))
        f.write('\n')
    f.close()