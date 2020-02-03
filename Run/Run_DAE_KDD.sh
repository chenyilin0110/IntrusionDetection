#!/bin/bash
train="train"
test="test"
outputLayer="2"
epoch="100"

END=20

for i in $(seq 1 $END);
do
    python3 src/DAE_KDD99/main.py $train $test $outputLayer $epoch
done