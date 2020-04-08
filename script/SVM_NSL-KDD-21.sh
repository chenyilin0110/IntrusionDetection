#!/bin/bash

train="train"
test="test-21"
c="1000"

END=5

# SVM 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_2-21.txt
    else
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_2-21.txt &
    fi
done

# SVM 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_5-21.txt
    else
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_5-21.txt &
    fi
done