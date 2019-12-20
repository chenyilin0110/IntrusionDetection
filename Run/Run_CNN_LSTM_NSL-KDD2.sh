#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="5"
batchsize="100"
epoch="100"
END=5

learning_rate="0.11"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.12"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.13"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.14"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done

learning_rate="0.15"
for i in $(seq 1 $END);
do
    python3 src/CNN_LSTM_NSL-KDD/main.py $train $test $test_21 $outputLayer $batchsize $epoch $learning_rate
done