#!/bin/bash
rm src/Plot/*/*/NSL-*
rm src/Plot/*/*/ICS_*
rm src/Plot/*/*/KDD*

dataset="NSL-KDD"
# NSL-KDD 2 categories
file_name="experimental_result_2"
path="src/Plot/NSL-KDD/2class/NSL-KDD_2class_Avg.txt"
echo -n '"'"NSL-KDD 2 categories"'" ' >> $path
python3 src/Calculate/calavg.py 5 DAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SNDAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 15 DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 DE_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 8 LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 3 HC_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_one_parameter $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 EDE_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 Naive_Bayes $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 RandomForest $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SVM $dataset $file_name >> $path

# NSL-KDD 5 categories
file_name="experimental_result_5"
path="src/Plot/NSL-KDD/5class/NSL-KDD_5class_Avg.txt"
echo -n '"'"NSL-KDD 5 categories"'" ' >> $path
python3 src/Calculate/calavg.py 5 DAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SNDAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 15 DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 DE_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 8 LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 3 HC_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_one_parameter $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 EDE_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 Naive_Bayes $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 RandomForest $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SVM $dataset $file_name >> $path

# NSL-KDD 2-21 categories
file_name="experimental_result_2-21"
path="src/Plot/NSL-KDD/2class/NSL-KDD_2class_Avg-21.txt"
echo -n '"'"NSL-KDD 2 categories-21"'" ' >> $path
python3 src/Calculate/calavg.py 5 DAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SNDAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 15 DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 DE_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 8 LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 3 HC_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_one_parameter $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 EDE_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 Naive_Bayes $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 RandomForest $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SVM $dataset $file_name >> $path

# NSL-KDD 5-21 categories
file_name="experimental_result_5-21"
path="src/Plot/NSL-KDD/5class/NSL-KDD_5class_Avg-21.txt"
echo -n '"'"NSL-KDD 5 categories-21"'" ' >> $path
python3 src/Calculate/calavg.py 5 DAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SNDAE $dataset $file_name >> $path
python3 src/Calculate/calavg.py 15 DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 3 DE_DNN $dataset $file_name >> $path
python3 src/Calculate/calavg.py 8 LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 3 HC_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_one_parameter $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
python3 src/Calculate/calavg.py 4 EDE_LSTM $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 Naive_Bayes $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 RandomForest $dataset $file_name >> $path
python3 src/Calculate/calavg.py 5 SVM $dataset $file_name >> $path

dataset="ICS"
data=15
# ICS 2 categories
for i in $(seq 1 $data)
do
    file_name="experimental_result_2-"$i
    path="src/Plot/ICS/2class/ICS_2class_Avg-"$i".txt"
    echo -n '"'"ICS 2 categories data "$i'" ' >> $path
    python3 src/Calculate/calavg.py 10 DAE $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 SNDAE $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 12 DNN $dataset $file_name >> $path
    # python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 DE_DNN $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 Naive_Bayes $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 RandomForest $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 SVM $dataset $file_name >> $path
done

# ICS 3 categories
for i in $(seq 1 $data)
do
    file_name="experimental_result_3-"$i
    path="src/Plot/ICS/3class/ICS_3class_Avg-"$i".txt"
    echo -n '"'"ICS 3 categories data "$i'" ' >> $path
    python3 src/Calculate/calavg.py 10 DAE $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 SNDAE $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 12 DNN $dataset $file_name >> $path
    # python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 DE_DNN $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 Naive_Bayes $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 RandomForest $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 SVM $dataset $file_name >> $path
done

# ICS multi categories
for i in $(seq 1 $data)
do
    file_name="experimental_result_41-"$i
    path="src/Plot/ICS/multi/ICS_multi_Avg-"$i".txt"
    echo -n '"'"ICS multi categories data "$i'" ' >> $path
    python3 src/Calculate/calavg.py 10 DAE $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 SNDAE $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 12 DNN $dataset $file_name >> $path
    # python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 DE_DNN $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 Naive_Bayes $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 RandomForest $dataset $file_name >> $path
    python3 src/Calculate/calavg.py 10 SVM $dataset $file_name >> $path
done
# dataset="KDD99"
# # KDD99 2 categories
# file_name="experimental_result_2"
# path="src/Plot/KDD99/2class/KDD99_2class_Avg.txt"
# echo '"'"KDD CUP 99 2 categories"'"' >> $path
# python3 src/Calculate/calavg.py 20 DAE $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 SNDAE $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 DE_DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 4 DE_LSTM_one_parameter $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 4 EDE_LSTM $dataset $file_name >> $path

# # KDD99 5 categories
# file_name="experimental_result_2"
# path="src/Plot/KDD99/2class/KDD99_2class_Avg.txt"
# echo '"'"KDD CUP 99 5 categories"'"' >> src/Plot/KDD99/5class/KDD99_2class_Avg.txt
# python3 src/Calculate/calavg.py 20 DAE $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 SNDAE $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 DE_DNN $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 10 HC_LSTM $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 4 DE_LSTM_one_parameter $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 4 DE_LSTM_two_parameters $dataset $file_name >> $path
# python3 src/Calculate/calavg.py 4 EDE_LSTM $dataset $file_name >> $path