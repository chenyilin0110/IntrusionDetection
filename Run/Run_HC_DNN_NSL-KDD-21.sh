#!/bin/bash
train="train"
test="test-21"
hiddenLayer="1"
outputLayer="2"
iteration="800"
epoch="100"

END=10
for i in $(seq 1 $END);
do
    python3 src/HC_DNN_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch
done