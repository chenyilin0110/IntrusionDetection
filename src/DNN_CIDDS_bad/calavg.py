import numpy as np
import sys

run = sys.argv[1]
name = sys.argv[2]
data = np.loadtxt('src/DNN_CIDDS_bad/result/' + name + '.txt', delimiter='\n')

print("neurons 50")
# calculate hidden layer = 1 and hidden neurons = 50
count_1_50 = 0
for i in range(0, int(run)):
    count_1_50 += data[i]
print("hidden layer = 1", count_1_50/int(run))
temp = int(run)

# calculate hidden layer = 2 and hidden neurons = 50
start = temp
end = start + int(run)
count_2_50 = 0
for i in range(start,end):
    count_2_50 += data[i]
print("hidden layer = 2", count_2_50/int(run))
temp = end

# calculate hidden layer = 3 and hidden neurons = 50
start = temp
end = start + int(run)
count_3_50 = 0
for i in range(start, end):
    count_3_50 += data[i]
print("hidden layer = 3", count_3_50/int(run))
temp = end

# calculate hidden layer = 4 and hidden neurons = 50
start = temp
end = start + int(run)
count_4_50 = 0
for i in range(start, end):
    count_4_50 += data[i]
print("hidden layer = 4", count_4_50/int(run))
temp = end

# calculate hidden layer = 5 and hidden neurons = 50
start = temp
end = start + int(run)
count_5_50 = 0
for i in range(start, end):
    count_5_50 += data[i]
print("hidden layer = 5", count_5_50/int(run))
temp = end

print("---------------------------------------------------------")

print("neurons 60")
# calculate hidden layer = 1 and hidden neurons = 60
start = temp
end = start + int(run)
count_1_60 = 0
for i in range(start, end):
    count_1_60 += data[i]
print("hidden layer = 1", count_1_60/int(run))
temp = end

# calculate hidden layer = 2 and hidden neurons = 60
start = temp
end = start + int(run)
count_2_60 = 0
for i in range(start,end):
    count_2_60 += data[i]
print("hidden layer = 2", count_2_60/int(run))
temp = end

# calculate hidden layer = 3 and hidden neurons = 60
start = temp
end = start + int(run)
count_3_60 = 0
for i in range(start, end):
    count_3_60 += data[i]
print("hidden layer = 3", count_3_60/int(run))
temp = end

# calculate hidden layer = 4 and hidden neurons = 60
start = temp
end = start + int(run)
count_4_60 = 0
for i in range(start, end):
    count_4_60 += data[i]
print("hidden layer = 4", count_4_60/int(run))
temp = end

# calculate hidden layer = 5 and hidden neurons = 60
start = temp
end = start + int(run)
count_5_60 = 0
for i in range(start, end):
    count_5_60 += data[i]
print("hidden layer = 5", count_5_60/int(run))
temp = end

print("---------------------------------------------------------")

print("neurons 70")
# calculate hidden layer = 1 and hidden neurons = 70
start = temp
end = start + int(run)
count_1_70 = 0
for i in range(start, end):
    count_1_70 += data[i]
print("hidden layer = 1", count_1_70/int(run))
temp = end

# calculate hidden layer = 2 and hidden neurons = 70
start = temp
end = start + int(run)
count_2_70 = 0
for i in range(start,end):
    count_2_70 += data[i]
print("hidden layer = 2", count_2_70/int(run))
temp = end

# calculate hidden layer = 3 and hidden neurons = 70
start = temp
end = start + int(run)
count_3_70 = 0
for i in range(start, end):
    count_3_70 += data[i]
print("hidden layer = 3", count_3_70/int(run))
temp = end

# calculate hidden layer = 4 and hidden neurons = 70
start = temp
end = start + int(run)
count_4_70 = 0
for i in range(start, end):
    count_4_70 += data[i]
print("hidden layer = 4", count_4_70/int(run))
temp = end

# calculate hidden layer = 5 and hidden neurons = 70
start = temp
end = start + int(run)
count_5_70 = 0
for i in range(start, end):
    count_5_70 += data[i]
print("hidden layer = 5", count_5_70/int(run))
temp = end

print("---------------------------------------------------------")

print("neurons 80")
# calculate hidden layer = 1 and hidden neurons = 80
start = temp
end = start + int(run)
count_1_80 = 0
for i in range(start, end):
    count_1_80 += data[i]
print("hidden layer = 1", count_1_80/int(run))
temp = end

# calculate hidden layer = 2 and hidden neurons = 80
start = temp
end = start + int(run)
count_2_80 = 0
for i in range(start,end):
    count_2_80 += data[i]
print("hidden layer = 2", count_2_80/int(run))
temp = end

# calculate hidden layer = 3 and hidden neurons = 80
start = temp
end = start + int(run)
count_3_80 = 0
for i in range(start, end):
    count_3_80 += data[i]
print("hidden layer = 3", count_3_80/int(run))
temp = end

# calculate hidden layer = 4 and hidden neurons = 80
start = temp
end = start + int(run)
count_4_80 = 0
for i in range(start, end):
    count_4_80 += data[i]
print("hidden layer = 4", count_4_80/int(run))
temp = end

# calculate hidden layer = 5 and hidden neurons = 80
start = temp
end = start + int(run)
count_5_80 = 0
for i in range(start, end):
    count_5_80 += data[i]
print("hidden layer = 5", count_5_80/int(run))
temp = end

print("---------------------------------------------------------")

print("neurons 90")
# calculate hidden layer = 1 and hidden neurons = 90
start = temp
end = start + int(run)
count_1_90 = 0
for i in range(start, end):
    count_1_90 += data[i]
print("hidden layer = 1", count_1_90/int(run))
temp = end

# calculate hidden layer = 2 and hidden neurons = 90
start = temp
end = start + int(run)
count_2_90 = 0
for i in range(start, end):
    count_2_90 += data[i]
print("hidden layer = 2", count_2_90/int(run))
temp = end

# calculate hidden layer = 3 and hidden neurons = 90
start = temp
end = start + int(run)
count_3_90 = 0
for i in range(start, end):
    count_3_90 += data[i]
print("hidden layer = 3", count_3_90/int(run))
temp = end

# calculate hidden layer = 4 and hidden neurons = 90
start = temp
end = start + int(run)
count_4_90 = 0
for i in range(start, end):
    count_4_90 += data[i]
print("hidden layer = 4", count_4_90/int(run))
temp = end

# calculate hidden layer = 5 and hidden neurons = 90
start = temp
end = start + int(run)
count_5_90 = 0
for i in range(start, end):
    count_5_90 += data[i]
print("hidden layer = 5", count_5_90/int(run))
temp = end

print("---------------------------------------------------------")

print("neurons 100")
# calculate hidden layer = 1 and hidden neurons = 100
start = temp
end = start + int(run)
count_1_100 = 0
for i in range(start, end):
    count_1_100 += data[i]
print("hidden layer = 1", count_1_100/int(run))
temp = end

# calculate hidden layer = 2 and hidden neurons = 100
start = temp
end = start + int(run)
count_2_100 = 0
for i in range(start, end):
    count_2_100 += data[i]
print("hidden layer = 2", count_2_100/int(run))
temp = end

# calculate hidden layer = 3 and hidden neurons = 100
start = temp
end = start + int(run)
count_3_100 = 0
for i in range(start, end):
    count_3_100 += data[i]
print("hidden layer = 3", count_3_100/int(run))
temp = end

# calculate hidden layer = 4 and hidden neurons = 100
start = temp
end = start + int(run)
count_4_100 = 0
for i in range(start, end):
    count_4_100 += data[i]
print("hidden layer = 4", count_4_100/int(run))
temp = end

# calculate hidden layer = 5 and hidden neurons = 100
start = temp
end = start + int(run)
count_5_100 = 0
for i in range(start, end):
    count_5_100 += data[i]
print("hidden layer = 5", count_5_100/int(run))
temp = end