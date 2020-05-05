#!/bin/bash
train="train"
test="test"

END=10
mid=`expr $END / 2`

# DAE 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/Naive_Bayes_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" % "$mid" ]
    then
        python3 src/Naive_Bayes_KDD99/main.py $train $test $outputLayer >> $path
    else
        python3 src/Naive_Bayes_KDD99/main.py $train $test $outputLayer >> $path &
    fi
done

# DAE 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/Naive_Bayes_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" % "$END" ]
    then
        python3 src/Naive_Bayes_KDD99/main.py $train $test $outputLayer >> $path
    else
        python3 src/Naive_Bayes_KDD99/main.py $train $test $outputLayer >> $path &
    fi
done