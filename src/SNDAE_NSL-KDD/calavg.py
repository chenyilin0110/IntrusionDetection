import numpy as np
import sys

run = sys.argv[1]
name = sys.argv[2]
data = np.loadtxt('src/SNDAE_NSL-KDD/result/' + name + '.txt', delimiter='\n')


print("tree = 10, ", end='')
count_10 = 0
for i in range(0, int(run)):
    count_10 += data[i]
print(count_10/int(run))
temp = int(run)

start = temp
end = start + int(run)
print("tree = 20, ", end='')
count_20 = 0
for i in range(start, end):
    count_20 += data[i]
print(count_20/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 30, ", end='')
count_30 = 0
for i in range(start, end):
    count_30 += data[i]
print(count_30/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 40, ", end='')
count_40 = 0
for i in range(start, end):
    count_40 += data[i]
print(count_40/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 50, ", end='')
count_50 = 0
for i in range(start, end):
    count_50 += data[i]
print(count_50/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 60, ", end='')
count_60 = 0
for i in range(start, end):
    count_60 += data[i]
print(count_60/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 70, ", end='')
count_70 = 0
for i in range(start, end):
    count_70 += data[i]
print(count_70/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 80, ", end='')
count_80 = 0
for i in range(start, end):
    count_80 += data[i]
print(count_80/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 90, ", end='')
count_90 = 0
for i in range(start, end):
    count_90 += data[i]
print(count_90/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 100, ", end='')
count_100 = 0
for i in range(start, end):
    count_100 += data[i]
print(count_100/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 110, ", end='')
count_110 = 0
for i in range(start, end):
    count_110 += data[i]
print(count_110/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 120, ", end='')
count_120 = 0
for i in range(start, end):
    count_120 += data[i]
print(count_120/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 130, ", end='')
count_130 = 0
for i in range(start, end):
    count_130 += data[i]
print(count_130/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 140, ", end='')
count_140 = 0
for i in range(start, end):
    count_140 += data[i]
print(count_140/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 150, ", end='')
count_150 = 0
for i in range(start, end):
    count_150 += data[i]
print(count_150/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 160, ", end='')
count_160 = 0
for i in range(start, end):
    count_160 += data[i]
print(count_160/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 170, ", end='')
count_170 = 0
for i in range(start, end):
    count_170 += data[i]
print(count_170/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 180, ", end='')
count_180 = 0
for i in range(start, end):
    count_180 += data[i]
print(count_180/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 190, ", end='')
count_190 = 0
for i in range(start, end):
    count_190 += data[i]
print(count_190/int(run))
temp = end

start = temp
end = start + int(run)
print("tree = 200, ", end='')
count_200 = 0
for i in range(start, end):
    count_200 += data[i]
print(count_200/int(run))
temp = end