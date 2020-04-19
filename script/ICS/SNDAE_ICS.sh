#!/bin/bash
test=20
tree_number=100

data=15
END=10

# SNDAE 2 categories
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

# SNDAE 3 categories
finder="3"
outputLayer="3"
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

# SNDAE multi categories
finder="multi"
outputLayer="41"
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