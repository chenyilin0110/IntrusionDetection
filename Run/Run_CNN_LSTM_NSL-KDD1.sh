#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="5"
batchsize="100"
epoch="100"
END=5

learning_rate="0.06"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.07"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.08"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.09"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.1"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done