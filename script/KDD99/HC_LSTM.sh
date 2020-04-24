#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
iteration="40"
batchSize="10000"
epoch="100"

END=3

# HC_LSTM 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/HC_LSTM_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/HC_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $batchSize $epoch >> $path
    else
        python3 src/HC_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $batchSize $epoch >> $path &
    fi
done

# HC_LSTM 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/HC_LSTM_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/HC_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $batchSize $epoch >> $path
    else
        python3 src/HC_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $batchSize $epoch >> $path &
    fi
done