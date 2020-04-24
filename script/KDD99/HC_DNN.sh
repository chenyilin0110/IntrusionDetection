#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
iteration="40"
epoch="100"

END=10

# HC_DNN 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/HC_DNN_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/HC_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch >> $path
    else
        python3 src/HC_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch >> $path &
    fi
done

# HC_DNN 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/HC_DNN_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/HC_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch >> $path
    else
        python3 src/HC_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch >> $path &
    fi
done