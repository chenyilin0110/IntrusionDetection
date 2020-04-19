#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
outputLayer="2"
iteration="40"
batchSize="10000"
epoch="100"

END=10
for i in $(seq 1 $END);
do
    python3 src/HC_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $batchSize $epoch
done