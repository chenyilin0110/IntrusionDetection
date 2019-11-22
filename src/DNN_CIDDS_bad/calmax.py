import numpy as np
import sys

run = sys.argv[1]
name = sys.argv[2]
data = np.loadtxt('src/DNN_CIDDS_bad/result/' + name + '.txt', delimiter='\n')

print("neurons 80")
# calculate hidden layer = 1 and hidden neurons = 80
count_1_80 = []
for i in range(0,int(run)):
    count_1_80.append(data[i])
print("hidden layer = 1", max(count_1_80))

# calculate hidden layer = 2 and hidden neurons = 80
start = int(run) - 1
end = int(run) * 2 - 1
count_2_80 = []
for i in range(start,end):
    count_2_80.append(data[i])
print("hidden layer = 2", max(count_2_80))

# calculate hidden layer = 3 and hidden neurons = 80
start = int(run) * 2 - 1
end = int(run) * 3 - 1
count_3_80 = []
for i in range(start,end):
    count_3_80.append(data[i])
print("hidden layer = 3", max(count_3_80))

# calculate hidden layer = 4 and hidden neurons = 80
start = int(run) * 3 - 1
end = int(run) * 4 - 1
count_4_80 = []
for i in range(start,end):
    count_4_80.append(data[i])
print("hidden layer = 4", max(count_4_80))

# calculate hidden layer = 5 and hidden neurons = 80
start = int(run) * 4 - 1
end = int(run) * 5 - 1
count_5_80 = []
for i in range(start,end):
    count_5_80.append(data[i])
print("hidden layer = 5", max(count_5_80))

print("---------------------------------------------------------")
print("neurons 90")
# calculate hidden layer = 1 and hidden neurons = 90
start = int(run) * 5 - 1
end = int(run) * 6 - 1
count_1_90 = []
for i in range(start,end):
    count_1_90.append(data[i])
print("hidden layer = 1", max(count_1_90))

# calculate hidden layer = 2 and hidden neurons = 90
start = int(run) * 6 - 1
end = int(run) * 7 - 1
count_2_90 = []
for i in range(start,end):
    count_2_90.append(data[i])
print("hidden layer = 2", max(count_2_90))

# calculate hidden layer = 3 and hidden neurons = 90
start = int(run) * 7 - 1
end = int(run) * 8 - 1
count_3_90 = []
for i in range(start,end):
    count_3_90.append(data[i])
print("hidden layer = 3", max(count_3_90))

# calculate hidden layer = 4 and hidden neurons = 90
start = int(run) * 8 - 1
end = int(run) * 9 - 1
count_4_90 = []
for i in range(start,end):
    count_4_90.append(data[i])
print("hidden layer = 4", max(count_4_90))

# calculate hidden layer = 5 and hidden neurons = 90
start = int(run) * 9 - 1
end = int(run) * 10 - 1
count_5_90 = []
for i in range(start,end):
    count_5_90.append(data[i])
print("hidden layer = 5", max(count_5_90))

print("---------------------------------------------------------")
print("neurons 100")
# calculate hidden layer = 1 and hidden neurons = 100
start = int(run) * 10 - 1
end = int(run) * 11 - 1
count_1_100 = []
for i in range(start,end):
    count_1_100.append(data[i])
print("hidden layer = 1", max(count_1_100))

# calculate hidden layer = 2 and hidden neurons = 100
start = int(run) * 11 - 1
end = int(run) * 12 - 1
count_2_100 = []
for i in range(start,end):
    count_2_100.append(data[i])
print("hidden layer = 2", max(count_2_100))

# calculate hidden layer = 3 and hidden neurons = 100
start = int(run) * 12 - 1
end = int(run) * 13 - 1
count_3_100 = []
for i in range(start,end):
    count_3_100.append(data[i])
print("hidden layer = 3", max(count_3_100))

# calculate hidden layer = 4 and hidden neurons = 100
start = int(run) * 13 - 1
end = int(run) * 14 - 1
count_4_100 = []
for i in range(start,end):
    count_4_100.append(data[i])
print("hidden layer = 4", max(count_4_100))

# calculate hidden layer = 5 and hidden neurons = 100
start = int(run) * 14 - 1
end = int(run) * 15 - 1
count_5_100 = []
for i in range(start,end):
    count_5_100.append(data[i])
print("hidden layer = 5", max(count_5_100))