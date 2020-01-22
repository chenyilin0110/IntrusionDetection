#!/bin/bash
train="train"
test="test"
outputLayer="2"
batchSize="10000"
epoch="100"

END=10
for i in $(seq 1 $END);
do
    python3 src/LSTM_KDD99/main.py $train $test $outputLayer $batchSize $epoch
done