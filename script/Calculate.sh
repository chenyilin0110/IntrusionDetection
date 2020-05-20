#!/bin/bash
rm src/Plot/NSL-KDD/*/NSL-*
rm src/Plot/*/*/ICS_*
rm src/Plot/*/*/KDD*

run="5"
#-----------------------------DE_LSTM get each run accuracy-----------------------------#
#------------------------delete avg file------------------------#
rm src/DE_LSTM_ICS/result/experimental_result_2-1.txt
rm src/DE_LSTM_ICS/result/experimental_result_2-2.txt
rm src/DE_LSTM_ICS/result/experimental_result_2-3.txt
rm src/DE_LSTM_ICS/result/experimental_result_3-1.txt
rm src/DE_LSTM_ICS/result/experimental_result_3-2.txt
rm src/DE_LSTM_ICS/result/experimental_result_3-3.txt
rm src/DE_LSTM_ICS/result/experimental_result_41-1.txt
rm src/DE_LSTM_ICS/result/experimental_result_41-2.txt
rm src/DE_LSTM_ICS/result/experimental_result_41-3.txt
rm src/DE_LSTM_KDD99/result/experimental_result_2.txt
rm src/DE_LSTM_KDD99/result/experimental_result_5.txt
rm src/DE_LSTM_NSL-KDD/result/experimental_result_2.txt
rm src/DE_LSTM_NSL-KDD/result/experimental_result_2-21.txt
rm src/DE_LSTM_NSL-KDD/result/experimental_result_5.txt
rm src/DE_LSTM_NSL-KDD/result/experimental_result_5-21.txt
#------------------------delete avg file------------------------#
algorithm="DE_LSTM"

dataset="ICS"
datasetNumner="3" # ICS data1 to data3
categories="2"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run $datasetNumner
categories="3"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run $datasetNumner
categories="41"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run $datasetNumner

dataset="KDD99"
categories="2"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run
categories="5"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run

dataset="NSL-KDD"
categories="2"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run
categories="5"
python3 src/Other/getAccuracy.py $algorithm $dataset $categories $run
#-----------------------------DE_LSTM get each run accuracy-----------------------------#

#-----------------------------NSL-KDD dataset-----------------------------#
dataset="NSL-KDD"
# 2 categories
file_name="experimental_result_2"
path="src/Plot/NSL-KDD/2class/NSL-KDD_2class_Avg.txt"
echo -n '"'"NSL-KDD 2 categories"'" ' >> $path
python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 EDE_LSTM $dataset $file_name >> $path

# 5 categories
file_name="experimental_result_5"
path="src/Plot/NSL-KDD/5class/NSL-KDD_5class_Avg.txt"
echo -n '"'"NSL-KDD 5 categories"'" ' >> $path
python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 EDE_LSTM $dataset $file_name >> $path

# 2-21 categories
file_name="experimental_result_2-21"
path="src/Plot/NSL-KDD/2class/NSL-KDD_2class_Avg-21.txt"
echo -n '"'"NSL-KDD 2 categories-21"'" ' >> $path
python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 EDE_LSTM $dataset $file_name >> $path

# 5-21 categories
file_name="experimental_result_5-21"
path="src/Plot/NSL-KDD/5class/NSL-KDD_5class_Avg-21.txt"
echo -n '"'"NSL-KDD 5 categories-21"'" ' >> $path
python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
# python3 src/Other/calavg.py 4 EDE_LSTM $dataset $file_name >> $path

#-----------------------------NSL-KDD dataset-----------------------------#

#-----------------------------ICS     dataset-----------------------------#
dataset="ICS"
data=3
# 2 categories
for i in $(seq 1 $data)
do
    file_name="experimental_result_2-"$i
    path="src/Plot/ICS/2class/ICS_2class_Avg.txt"
    echo -n '"'"DS"$i'" ' >> $path
    python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
    python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
    python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
    python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
    python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
    echo >> $path
done

# 3 categories
for i in $(seq 1 $data)
do
    file_name="experimental_result_3-"$i
    path="src/Plot/ICS/3class/ICS_3class_Avg.txt"
    echo -n '"'"DS"$i'" ' >> $path
    python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
    python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
    python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
    python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
    python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
    echo >> $path
done

# multi categories
for i in $(seq 1 $data)
do
    file_name="experimental_result_41-"$i
    path="src/Plot/ICS/multi/ICS_multi_Avg.txt"
    echo -n '"'"DS"$i'" ' >> $path
    python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
    python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
    python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
    python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
    python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
    python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
    echo >> $path
done
#-----------------------------ICS     dataset-----------------------------#

#-----------------------------KDD99   dataset-----------------------------#
dataset="KDD99"
# 2 categories
file_name="experimental_result_2"
path="src/Plot/KDD99/2class/KDD99_2class_Avg.txt"
echo -n '"'"KDD CUP 99 2 categories"'" ' >> $path
python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path

# 5 categories
file_name="experimental_result_5"
path="src/Plot/KDD99/5class/KDD99_5class_Avg.txt"
echo -n '"'"KDD CUP 99 5 categories"'" ' >> $path
python3 src/Other/calavg.py $run DAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run SNDAE $dataset $file_name >> $path
python3 src/Other/calavg.py $run DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_DNN $dataset $file_name >> $path
python3 src/Other/calavg.py $run LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run DE_LSTM $dataset $file_name >> $path
python3 src/Other/calavg.py $run Naive_Bayes $dataset $file_name >> $path
python3 src/Other/calavg.py $run RandomForest $dataset $file_name >> $path
python3 src/Other/calavg.py $run SVM $dataset $file_name >> $path
python3 src/Other/calavg.py $run KNN $dataset $file_name >> $path
#-----------------------------KDD99   dataset-----------------------------#