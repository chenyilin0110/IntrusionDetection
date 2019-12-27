#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
outputLayer="5"
batchSize="10000"
iteration="40"
epoch="100"
population="20"
F="0.5"
CR="0.3"

END=2
for i in $(seq 1 $END);
do
    python3 src/DE_LSTM_KDD99_cuda/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR
done