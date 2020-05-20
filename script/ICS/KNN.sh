#!/bin/bash
test=20

data=3
END=5

# KNN 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/KNN_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/KNN_ICS/main.py $finder $filename $outputLayer $test $c >> $path
        else
            python3 src/KNN_ICS/main.py $finder $filename $outputLayer $test $c >> $path &
        fi
    done
done

# KNN 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/KNN_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/KNN_ICS/main.py $finder $filename $outputLayer $test $c >> $path
        else
            python3 src/KNN_ICS/main.py $finder $filename $outputLayer $test $c >> $path &
        fi
    done
done

# KNN multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/KNN_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/KNN_ICS/main.py $finder $filename $outputLayer $test $c >> $path
        else
            python3 src/KNN_ICS/main.py $finder $filename $outputLayer $test $c >> $path &
        fi
    done
done