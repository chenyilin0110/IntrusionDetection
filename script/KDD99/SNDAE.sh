#!/bin/bash
train="train"
test="test"
tree="160"
learning_rate="0.14"

END=4

# SNDAE 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/SNDAE_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate >> $path
    else
        python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate >> $path &
    fi
    
done

# SNDAE 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/SNDAE_KDD99/result/experimental_result_"$outputLayer".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate >> $path
    else
        python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate >> $path &
    fi
done