#!/bin/bash
train="train"
test="test-21"
hiddenLayer="1"
outputLayer="2"
iteration="40"
epoch="100"
population="20"
F="0.5"
CR="0.3"
name="-21"

END=5
for i in $(seq 1 $END);
do
    python3.6 src/DE_DNN_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR
done