#!/bin/bash

train="train"
test="test"
c="1000"

END=5

# SVM 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_2.txt
    else
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_2.txt &
    fi
done

# SVM 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_5.txt
    else
        python3 src/SVM/main.py $train $test $outputLayer $c >> src/SVM/result/experimental_result_5.txt &
    fi
done