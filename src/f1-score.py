import numpy as np
f = open('src/Plot/ICS/multi/f1-score.txt', "a")
pre = np.loadtxt('src/Plot/ICS/multi/ICS_multi_precision_Avg' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/ICS/multi/ICS_multi_recall_Avg' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "DS1" + '\" ')
for i in range(1,11):
    count = (2 * float(pre[0][i]) * float(re[0][i]) / (float(pre[0][i]) + float(re[0][i])))
    f.write(str(count) + ' ') 
f.write("\n")
f.write('\"' + "DS2" + '\" ')
for i in range(1,11):
    count = (2 * float(pre[1][i]) * float(re[1][i]) / (float(pre[1][i]) + float(re[1][i])))
    f.write(str(count) + ' ') 
f.write("\n")
f.write('\"' + "DS3" + '\" ')
for i in range(1,11):
    count = (2 * float(pre[2][i]) * float(re[2][i]) / (float(pre[2][i]) + float(re[2][i])))
    f.write(str(count) + ' ') 
f.close()


f = open('src/Plot/KDD99/2class/f1-score.txt', "a")
pre = np.loadtxt('src/Plot/KDD99/2class/KDD99_2class_precision_Avg' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/KDD99/2class/KDD99_2class_recall_Avg' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "KDD CUP 99 2 categories" + '\" ')
for i in range(5,14):
    count = (2 * float(pre[i]) * float(re[i]) / (float(pre[i]) + float(re[i])))
    f.write(str(count) + ' ') 
f.close()

f = open('src/Plot/KDD99/5class/f1-score.txt', "a")
pre = np.loadtxt('src/Plot/KDD99/5class/KDD99_5class_precision_Avg' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/KDD99/5class/KDD99_5class_recall_Avg' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "KDD CUP 99 5 categories" + '\" ')
for i in range(5,14):
    count = (2 * float(pre[i]) * float(re[i]) / (float(pre[i]) + float(re[i])))
    f.write(str(count) + ' ') 
# f.close()

f = open('src/Plot/NSL-KDD/2class/f1-score.txt', "a")
pre = np.loadtxt('src/Plot/NSL-KDD/2class/NSL-KDD_2class_precision_Avg' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "NSL-KDD 2 categories" + '\" ')
for i in range(3,13):
    count = (2 * float(pre[i]) * float(re[i]) / (float(pre[i]) + float(re[i])))
    f.write(str(count) + ' ') 
f.close()

f = open('src/Plot/NSL-KDD/5class/f1-score.txt', "a")
pre = np.loadtxt('src/Plot/NSL-KDD/5class/NSL-KDD_5class_precision_Avg' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/NSL-KDD/5class/NSL-KDD_5class_recall_Avg' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "NSL-KDD 5 categories" + '\" ')
for i in range(3,13):
    count = (2 * float(pre[i]) * float(re[i]) / (float(pre[i]) + float(re[i])))
    f.write(str(count) + ' ') 
f.close()

f = open('src/Plot/NSL-KDD/2class/f1-score-21.txt', "a")
pre = np.loadtxt('src/Plot/NSL-KDD/2class/NSL-KDD_2class_precision_Avg-21' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "NSL-KDD 2 categories-21" + '\" ')
for i in range(3,13):
    count = (2 * float(pre[i]) * float(re[i]) / (float(pre[i]) + float(re[i])))
    f.write(str(count) + ' ') 
f.close()

f = open('src/Plot/NSL-KDD/5class/f1-score-21.txt', "a")
pre = np.loadtxt('src/Plot/NSL-KDD/5class/NSL-KDD_5class_precision_Avg-21' + '.txt',dtype=np.str)
re = np.loadtxt('src/Plot/NSL-KDD/5class/NSL-KDD_5class_recall_Avg-21' + '.txt', dtype=np.str)
count = 0.0
f.write('\"' + "NSL-KDD 5 categories-21" + '\" ')
for i in range(3,13):
    count = (2 * float(pre[i]) * float(re[i]) / (float(pre[i]) + float(re[i])))
    f.write(str(count) + ' ') 
f.close()