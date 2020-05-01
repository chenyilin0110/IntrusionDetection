#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
iteration="40"
epoch="100"
population="20"
F="0.5"
CR="0.3"

END=9
max=3
CUDA_VISIBLE_DEVICES=0 

# DE_DNN 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/DE_DNN_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    temp=`expr $i % $max`
    if [ "$temp" = "0" ]
    then
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR $i >> $path
    else
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR $i >> $path &
    fi
done

# DE_DNN 5 categories
temp=0
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/DE_DNN_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    temp=`expr $i % $max`
    if [ "$temp" = "0" ]
    then
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR $i >> $path
    else
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR $i >> $path &
    fi
done