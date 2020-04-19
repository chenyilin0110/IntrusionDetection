#!/bin/bash
test=20
epoch=100

data=15
END=10

# DAE 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/DAE_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/DAE_ICS/main.py $finder $filename $outputLayer $test $epoch $j >> $path
        else
            python3 src/DAE_ICS/main.py $finder $filename $outputLayer $test $epoch $j >> $path &
        fi
    done
done

# DAE 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/DAE_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/DAE_ICS/main.py $finder $filename $outputLayer $test $epoch $j >> $path
        else
            python3 src/DAE_ICS/main.py $finder $filename $outputLayer $test $epoch $j >> $path &
        fi
    done
done

# DAE multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/DAE_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/DAE_ICS/main.py $finder $filename $outputLayer $test $epoch $j >> $path
        else
            python3 src/DAE_ICS/main.py $finder $filename $outputLayer $test $epoch $j >> $path &
        fi
    done
done