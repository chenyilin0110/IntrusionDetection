#!/bin/bash
train="train"
test="test"
C=0.1

END=10
max=`expr $END / 2`

# DAE 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/SVM_KDD99/result/experimental_result_"$outputLayer".txt"
    temp=`expr $i % $max`
    if [ "$temp" = "0" ]
    then
        python3 src/SVM_KDD99/main.py $train $test $outputLayer $C >> $path
    else
        python3 src/SVM_KDD99/main.py $train $test $outputLayer $C >> $path &
    fi
done

# DAE 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/SVM_KDD99/result/experimental_result_"$outputLayer".txt"
    temp=`expr $i % $max`
    if [ "$temp" = "0" ]
    then
        python3 src/SVM_KDD99/main.py $train $test $outputLayer $C >> $path
    else
        python3 src/SVM_KDD99/main.py $train $test $outputLayer $C >> $path &
    fi
done