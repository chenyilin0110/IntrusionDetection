import numpy as np
import sys

finder = sys.argv[1]
filename = sys.argv[2]
run = sys.argv[3]
output = sys.argv[4]

dataset = np.loadtxt(finder+'/'+filename, dtype=np.str, delimiter='\n')
temp=dataset[:]
accuracy = np.zeros(int(run))
f1score = np.zeros(int(run))
precision = np.zeros(int(run))
recall = np.zeros(int(run))

for i in range(int(run)):
    j = i * 5
    accuracy[i] = temp[j]
    f1score[i] = temp[j+1]
    precision[i] = temp[j+3]
    recall[i] = temp[j+4]
accuracy = accuracy.astype(float)
f1score = f1score.astype(float)
precision = precision.astype(float)
recall = recall.astype(float)

if output == "accuracy":
    data = accuracy
elif output == "f1score":
    data = f1score
elif output == "precision":
    data = precision
else:
    data = recall

total = 0
for i in range(len(data)):
    total += data[i]
total = total/int(run)
print(total)