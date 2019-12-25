#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
outputLayer="5"
iteration="40"
epoch="100"

END=10
for i in $(seq 1 $END);
do
    python3 src/HC_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch
done