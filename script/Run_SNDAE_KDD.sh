#!/bin/bash
train="train"
test="test"
outputLayer="2"
tree="160"
END=5

learning_rate="0.14"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done