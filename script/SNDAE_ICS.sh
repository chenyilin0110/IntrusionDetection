#!/bin/bash
test=20
tree_number=100

data=15
END=10

# DAE 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/SNDAE_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/SNDAE_ICS/main.py $finder $filename $outputLayer $test $tree_number $j >> $path
        else
            python3 src/SNDAE_ICS/main.py $finder $filename $outputLayer $test $tree_number $j >> $path &
        fi
    done
done

# DAE 5 categories
finder="5"
outputLayer="5"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/SNDAE_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/SNDAE_ICS/main.py $finder $filename $outputLayer $test $tree_number $j >> $path
        else
            python3 src/SNDAE_ICS/main.py $finder $filename $outputLayer $test $tree_number $j >> $path &
        fi
    done
done

# DAE multi categories
finder="multi"
outputLayer="multi"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/SNDAE_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/SNDAE_ICS/main.py $finder $filename $outputLayer $test $tree_number $j >> $path
        else
            python3 src/SNDAE_ICS/main.py $finder $filename $outputLayer $test $tree_number $j >> $path &
        fi
    done
done