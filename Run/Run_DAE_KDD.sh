#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="2"
epoch="100"

END=10
learning_rate="0.01"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done