#!/bin/bash

train="train"
test="test"
estimators="100"

END=5

# Random Forest 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/RandomForest_NSL-KDD/main.py $train $test $outputLayer $estimators >> src/RandomForest_NSL-KDD/result/experimental_result_2.txt
    else
        python3 src/RandomForest_NSL-KDD/main.py $train $test $outputLayer $estimators >> src/RandomForest_NSL-KDD/result/experimental_result_2.txt &
    fi
done

# Random Forest 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/RandomForest_NSL-KDD/main.py $train $test $outputLayer $estimators >> src/RandomForest_NSL-KDD/result/experimental_result_5.txt
    else
        python3 src/RandomForest_NSL-KDD/main.py $train $test $outputLayer $estimators >> src/RandomForest_NSL-KDD/result/experimental_result_5.txt &
    fi
done