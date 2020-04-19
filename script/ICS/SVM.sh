#!/bin/bash
test=20
c=1000

data=15
END=10

# SVM 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/SVM_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/SVM_ICS/main.py $finder $filename $outputLayer $test $c >> $path
        else
            python3 src/SVM_ICS/main.py $finder $filename $outputLayer $test $c >> $path &
        fi
    done
done

# SVM 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/SVM_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/SVM_ICS/main.py $finder $filename $outputLayer $test $c >> $path
        else
            python3 src/SVM_ICS/main.py $finder $filename $outputLayer $test $c >> $path &
        fi
    done
done

# SVM multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/SVM_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/SVM_ICS/main.py $finder $filename $outputLayer $test $c >> $path
        else
            python3 src/SVM_ICS/main.py $finder $filename $outputLayer $test $c >> $path &
        fi
    done
done