#!/bin/bash
hiddenLayer=3
hiddenNeural=80
test=20
iteration=40
epoch=100
population=20
F=0.5
CR=0.3

data=15
END=10

# DAE 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/DE_DNN_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path
        else
            python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
        fi
    done
done

# DAE 5 categories
finder="5"
outputLayer="5"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/DE_DNN_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path
        else
            python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
        fi
    done
done

# DAE multi categories
finder="multi"
outputLayer="multi"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/DE_DNN_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path
        else
            python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
        fi
    done
done