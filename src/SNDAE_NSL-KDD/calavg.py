import numpy as np
import sys

run = sys.argv[1]
name = sys.argv[2]
data = np.loadtxt('src/SNDAE_NSL-KDD/result/' + name + '.txt', delimiter='\n')
print("max index, max value =", np.argmax(data), ",", np.max(data))
avg_list = []

count = 0
for i in range(len(data)):
    if i % int(run) == 0 and i > 0:
        avg_list.append(count/int(run))
        count = data[i]
    else:
        count += data[i]
        if i == len(data) - 1:
            avg_list.append(count/int(run))

print("avg: tree =", (avg_list.index(max(avg_list)) + 1 ) * int(run), ",", max(avg_list))