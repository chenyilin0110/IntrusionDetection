#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="2"
tree="90"
learning_rate="0.02"
END=5
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree $learning_rate
done