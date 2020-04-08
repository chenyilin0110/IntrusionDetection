#!/bin/bash

train="train"
test="test-21"

END=5

# Naive Bayes 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/Naive_Bayes/main.py $train $test $outputLayer >> src/Naive_Bayes/result/experimental_result_2-21.txt
    else
        python3 src/Naive_Bayes/main.py $train $test $outputLayer >> src/Naive_Bayes/result/experimental_result_2-21.txt &
    fi
done

# Naive Bayes 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    if [ "$i" = "$END" ]
    then
        python3 src/Naive_Bayes/main.py $train $test $outputLayer >> src/Naive_Bayes/result/experimental_result_5-21.txt
    else
        python3 src/Naive_Bayes/main.py $train $test $outputLayer >> src/Naive_Bayes/result/experimental_result_5-21.txt &
    fi
done