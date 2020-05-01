#!/bin/bash
train="train"
test="test"
batchSize="2560"
epoch="100"

END=8

# LSTM 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/LSTM_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/LSTM_KDD99/main.py $train $test $outputLayer $batchSize $epoch >> $path
    else
        python3 src/LSTM_KDD99/main.py $train $test $outputLayer $batchSize $epoch >> $path &
    fi
done

# LSTM 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/LSTM_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/LSTM_KDD99/main.py $train $test $outputLayer $batchSize $epoch >> $path
    else
        python3 src/LSTM_KDD99/main.py $train $test $outputLayer $batchSize $epoch >> $path &
    fi
done