#!/bin/bash
train="train"
test="test"
epoch="100"

END=5

# DAE 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/DAE_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/DAE_KDD99/main.py $train $test $outputLayer $epoch >> $path
    else
        python3 src/DAE_KDD99/main.py $train $test $outputLayer $epoch >> $path &
    fi
done

# DAE 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/DAE_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/DAE_KDD99/main.py $train $test $outputLayer $epoch >> $path
    else
        python3 src/DAE_KDD99/main.py $train $test $outputLayer $epoch >> $path &
    fi
done