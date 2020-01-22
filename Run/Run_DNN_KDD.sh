#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
hiddenNeural="80"
outputLayer="2"
epoch="100"

END=10
for i in $(seq 1 $END);
do
    python3 src/DNN_KDD99/main.py $train $test $hiddenLayer $hiddenNeural $outputLayer $epoch
done