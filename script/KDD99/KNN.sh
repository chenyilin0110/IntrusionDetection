#!/bin/bash
train="train"
test="test"

END=5

# KNN 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/KNN_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ $i = $END ]
    then
        python3 src/KNN_KDD99/main.py $train $test $outputLayer $C >> $path
    else
        python3 src/KNN_KDD99/main.py $train $test $outputLayer $C >> $path &
    fi
done

# KNN 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/KNN_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ $i = $END ]
    then
        python3 src/KNN_KDD99/main.py $train $test $outputLayer $C >> $path
    else
        python3 src/KNN_KDD99/main.py $train $test $outputLayer $C >> $path &
    fi
done