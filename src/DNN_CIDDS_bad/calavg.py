import numpy as np
import sys

run = sys.argv[1]
name = sys.argv[2]
data = np.loadtxt('src/DNN_CIDDS_bad/result/' + name + '.txt', delimiter='\n')

print("neurons 80")
# calculate hidden layer = 1 and hidden neurons = 80
count_1_80 = 0
for i in range(0,int(run)):
    count_1_80 += data[i]
print("hidden layer = 1", count_1_80/int(run))

# calculate hidden layer = 2 and hidden neurons = 80
start = int(run) - 1
end = int(run) * 2 - 1
count_2_80 = 0
for i in range(start,end):
    count_2_80 += data[i]
print("hidden layer = 2", count_2_80/int(run))

# calculate hidden layer = 3 and hidden neurons = 80
start = int(run) * 2 - 1
end = int(run) * 3 - 1
count_3_80 = 0
for i in range(start, end):
    count_3_80 += data[i]
print("hidden layer = 3", count_3_80/int(run))

# calculate hidden layer = 4 and hidden neurons = 80
start = int(run) * 3 - 1
end = int(run) * 4 - 1
count_4_80 = 0
for i in range(start, end):
    count_4_80 += data[i]
print("hidden layer = 4", count_4_80/int(run))

# calculate hidden layer = 5 and hidden neurons = 80
start = int(run) * 4 - 1
end = int(run) * 5 - 1
count_5_80 = 0
for i in range(start, end):
    count_5_80 += data[i]
print("hidden layer = 5", count_5_80/int(run))

print("---------------------------------------------------------")
print("neurons 90")
# calculate hidden layer = 1 and hidden neurons = 90
start = int(run) * 5 - 1
end = int(run) * 6 - 1
count_1_90 = 0
for i in range(start, end):
    count_1_90 += data[i]
print("hidden layer = 1", count_1_90/int(run))

# calculate hidden layer = 2 and hidden neurons = 90
start = int(run) * 6 - 1
end = int(run) * 7 - 1
count_2_90 = 0
for i in range(start, end):
    count_2_90 += data[i]
print("hidden layer = 2", count_2_90/int(run))

# calculate hidden layer = 3 and hidden neurons = 90
start = int(run) * 7 - 1
end = int(run) * 8 - 1
count_3_90 = 0
for i in range(start, end):
    count_3_90 += data[i]
print("hidden layer = 3", count_3_90/int(run))

# calculate hidden layer = 4 and hidden neurons = 90
start = int(run) * 8 - 1
end = int(run) * 9 - 1
count_4_90 = 0
for i in range(start, end):
    count_4_90 += data[i]
print("hidden layer = 4", count_4_90/int(run))

# calculate hidden layer = 5 and hidden neurons = 90
start = int(run) * 9 - 1
end = int(run) * 10 - 1
count_5_90 = 0
for i in range(start, end):
    count_5_90 += data[i]
print("hidden layer = 5", count_5_90/int(run))

print("---------------------------------------------------------")
print("neurons 100")
# calculate hidden layer = 1 and hidden neurons = 100
start = int(run) * 10 - 1
end = int(run) * 11 - 1
count_1_100 = 0
for i in range(start, end):
    count_1_100 += data[i]
print("hidden layer = 1", count_1_100/int(run))

# calculate hidden layer = 2 and hidden neurons = 100
start = int(run) * 11 - 1
end = int(run) * 12 - 1
count_2_100 = 0
for i in range(start, end):
    count_2_100 += data[i]
print("hidden layer = 2", count_2_100/int(run))

# calculate hidden layer = 3 and hidden neurons = 100
start = int(run) * 12 - 1
end = int(run) * 13 - 1
count_3_100 = 0
for i in range(start, end):
    count_3_100 += data[i]
print("hidden layer = 3", count_3_100/int(run))

# calculate hidden layer = 4 and hidden neurons = 100
start = int(run) * 13 - 1
end = int(run) * 14 - 1
count_4_100 = 0
for i in range(start, end):
    count_4_100 += data[i]
print("hidden layer = 4", count_4_100/int(run))

# calculate hidden layer = 5 and hidden neurons = 100
start = int(run) * 14 - 1
end = int(run) * 15 - 1
count_5_100 = 0
for i in range(start, end):
    count_5_100 += data[i]
print("hidden layer = 5", count_5_100/int(run))