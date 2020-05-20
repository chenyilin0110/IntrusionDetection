#!/bin/bash

train="train"
test="test"

END=5

# KNN_NSL-KDD 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/KNN_NSL-KDD/main.py $train $test $outputLayer >> src/KNN_NSL-KDD/result/experimental_result_2.txt
    else
        python3 src/KNN_NSL-KDD/main.py $train $test $outputLayer >> src/KNN_NSL-KDD/result/experimental_result_2.txt &
    fi
done

# KNN_NSL-KDD 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/KNN_NSL-KDD/main.py $train $test $outputLayer >> src/KNN_NSL-KDD/result/experimental_result_5.txt
    else
        python3 src/KNN_NSL-KDD/main.py $train $test $outputLayer >> src/KNN_NSL-KDD/result/experimental_result_5.txt &
    fi
done