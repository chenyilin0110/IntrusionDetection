import numpy as np
import sys

algorithm = sys.argv[1]
dataset = sys.argv[2]
categories = sys.argv[3]
run = sys.argv[4]

if dataset == "ICS":
    datasetNumber = sys.argv[5]
    # copy acc to other file for ICS dataset
    for i in range(int(datasetNumber)):
        f = open('src/' + algorithm +'_' + dataset + '/result/' + 'experimental_result_' + categories + '-' + str(i+1) + '.txt', "a")
        for j in range(int(run)):
            data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'experimental_result_' + categories + '-' + str((i+1)) + '-' + str(j+1) + '.txt', delimiter='\n')
            f.write(str(data[-1]))
            f.write('\n')
        f.close()
else:
    # copy acc to other file for KDD99 & NSL-KDD dataset
    f = open('src/' + algorithm +'_' + dataset + '/result/' + 'experimental_result_' + categories + '.txt', "a")
    for j in range(int(run)):
        data = np.loadtxt('src/' + algorithm + '_' + dataset + '/result/' + 'experimental_result_' + categories + '-' + str(j+1) + '.txt', delimiter='\n')
        f.write(str(data[-1]))
        f.write('\n')
    f.close()