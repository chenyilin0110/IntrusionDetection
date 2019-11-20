import numpy as np
import sys

run = sys.argv[1]
name = sys.argv[2]
data = np.loadtxt('src/DNN_CIDDS_bad/result/' + name + '.txt', delimiter='\n')

print("neurons 80")
# calculate hidden layer = 1 and hidden neurons = 80
count_1_80 = []
for i in range(0,30):
    count_1_80.append(data[i])
print("hidden layer = 1", max(count_1_80))

# calculate hidden layer = 2 and hidden neurons = 80
count_2_80 = []
for i in range(29,59):
    count_2_80.append(data[i])
print("hidden layer = 2", max(count_2_80))

# calculate hidden layer = 3 and hidden neurons = 80
count_3_80 = []
for i in range(59,89):
    count_3_80.append(data[i])
print("hidden layer = 3", max(count_3_80))

# calculate hidden layer = 4 and hidden neurons = 80
count_4_80 = []
for i in range(89,119):
    count_4_80.append(data[i])
print("hidden layer = 4", max(count_4_80))

# calculate hidden layer = 5 and hidden neurons = 80
count_5_80 = []
for i in range(119,149):
    count_5_80.append(data[i])
print("hidden layer = 5", max(count_5_80))

print("---------------------------------------------------------")
print("neurons 90")
# calculate hidden layer = 1 and hidden neurons = 90
count_1_90 = []
for i in range(149,179):
    count_1_90.append(data[i])
print("hidden layer = 1", max(count_1_90))

# calculate hidden layer = 2 and hidden neurons = 90
count_2_90 = []
for i in range(179,209):
    count_2_90.append(data[i])
print("hidden layer = 2", max(count_2_90))

# calculate hidden layer = 3 and hidden neurons = 90
count_3_90 = []
for i in range(209,239):
    count_3_90.append(data[i])
print("hidden layer = 3", max(count_3_90))

# calculate hidden layer = 4 and hidden neurons = 90
count_4_90 = []
for i in range(239,269):
    count_4_90.append(data[i])
print("hidden layer = 4", max(count_4_90))

# calculate hidden layer = 5 and hidden neurons = 90
count_5_90 = []
for i in range(269,299):
    count_5_90.append(data[i])
print("hidden layer = 5", max(count_5_90))

print("---------------------------------------------------------")
print("neurons 100")
# calculate hidden layer = 1 and hidden neurons = 100
count_1_100 = []
for i in range(299,329):
    count_1_100.append(data[i])
print("hidden layer = 1", max(count_1_100))

# calculate hidden layer = 2 and hidden neurons = 100
count_2_100 = []
for i in range(329,359):
    count_2_100.append(data[i])
print("hidden layer = 2", max(count_2_100))

# calculate hidden layer = 3 and hidden neurons = 100
count_3_100 = []
for i in range(359,389):
    count_3_100.append(data[i])
print("hidden layer = 3", max(count_3_100))

# calculate hidden layer = 4 and hidden neurons = 100
count_4_100 = []
for i in range(389,419):
    count_4_100.append(data[i])
print("hidden layer = 4", max(count_4_100))

# calculate hidden layer = 5 and hidden neurons = 100
count_5_100 = []
for i in range(419,449):
    count_5_100.append(data[i])
print("hidden layer = 5", max(count_5_100))