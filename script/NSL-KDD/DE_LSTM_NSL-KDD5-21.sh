#!/bin/bash
train="train"
test="test-21"
hiddenLayer="1"
outputLayer="5"
batchSize="10000"
iteration="40"
epoch="80"
population="20"
F="0.5"
CR="0.3"
name="-21"

END=1
for i in $(seq 1 $END);
do
    python3.6 src/DE_LSTM_NSL-KDD_cuda/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $name
done