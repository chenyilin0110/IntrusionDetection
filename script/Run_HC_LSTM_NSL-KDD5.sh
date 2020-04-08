#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
outputLayer="5"
iteration="800"
batchSize="10000"
epoch="100"
name="0"

END=3
for i in $(seq 1 $END);
do
    CUDA_VISIBLE_DEVICES=1 python3.6 src/HC_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $iteration $batchSize $epoch $name
done