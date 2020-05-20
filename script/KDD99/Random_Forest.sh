#!/bin/bash
train="train"
test="test"
estimators=10

END=10
max=`expr $END / 2`

# Random Forest 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/RandomForest_KDD99/result/experimental_result_"$outputLayer".txt"
    temp=`expr $i % $max`
    if [ "$temp" = "0" ]
    then
        python3 src/RandomForest_KDD99/main.py $train $test $outputLayer $estimators >> $path
    else
        python3 src/RandomForest_KDD99/main.py $train $test $outputLayer $estimators >> $path &
    fi
done

# Random Forest 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/RandomForest_KDD99/result/experimental_result_"$outputLayer".txt"
    temp=`expr $i % $max`
    if [ "$temp" = "0" ]
    then
        python3 src/RandomForest_KDD99/main.py $train $test $outputLayer $estimators >> $path
    else
        python3 src/RandomForest_KDD99/main.py $train $test $outputLayer $estimators >> $path &
    fi
done