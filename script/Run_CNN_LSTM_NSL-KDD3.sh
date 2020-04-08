#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="5"
batchsize="100"
epoch="100"
END=5

learning_rate="0.16"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.17"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.18"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.19"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.2"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done