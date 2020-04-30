import numpy as np
import sys

run = sys.argv[1]
folder = sys.argv[2]
file_name = sys.argv[3]
data = np.loadtxt('src/' + folder + '/result/' + file_name + '.txt', delimiter='\n')
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

# lr
for each_lr in range(len(avg_list)):
    print("lr =",(each_lr + 1) / 100,avg_list[each_lr])
print("max index, max value =", np.argmax(data), ",", np.max(data))
print("avg: tree =", (avg_list.index(max(avg_list)) + 1 ) / 100, ",", max(avg_list))