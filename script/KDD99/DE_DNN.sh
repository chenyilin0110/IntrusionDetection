#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
iteration="40"
epoch="100"
population="20"
F="0.5"
CR="0.3"

END=5

# DE_DNN 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/DE_DNN_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR >> $path
    else
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR >> $path &
    fi
done

# DE_DNN 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/DE_DNN_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" = "$END" ]
    then
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR >> $path
    else
        python3 src/DE_DNN_KDD99/main.py $train $test $hiddenLayer $outputLayer $iteration $epoch $population $F $CR >> $path &
    fi
done