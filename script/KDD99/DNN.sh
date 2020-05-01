#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
hiddenNeural="80"
epoch="100"

END=15

# DNN 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/DNN_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/DNN_KDD99/main.py $train $test $hiddenLayer $hiddenNeural $outputLayer $epoch >> $path
    else
        python3 src/DNN_KDD99/main.py $train $test $hiddenLayer $hiddenNeural $outputLayer $epoch >> $path &
    fi
done

# DNN 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/DNN_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/DNN_KDD99/main.py $train $test $hiddenLayer $hiddenNeural $outputLayer $epoch >> $path
    else
        python3 src/DNN_KDD99/main.py $train $test $hiddenLayer $hiddenNeural $outputLayer $epoch >> $path &
    fi
done