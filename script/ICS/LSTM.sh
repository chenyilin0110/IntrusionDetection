#!/bin/bash
test=20
batchSize=256
epoch=100

data=15
END=10

# LSTM 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/LSTM_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/LSTM_ICS/main.py $finder $filename $outputLayer $test $batchSize $epoch $i >> $path
        else
            python3 src/LSTM_ICS/main.py $finder $filename $outputLayer $test $batchSize $epoch $i >> $path &
        fi
    done
done

# LSTM 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/LSTM_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/LSTM_ICS/main.py $finder $filename $outputLayer $test $batchSize $epoch $i >> $path
        else
            python3 src/LSTM_ICS/main.py $finder $filename $outputLayer $test $batchSize $epoch $i >> $path &
        fi
    done
done

# LSTM multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    path="src/LSTM_ICS/result/experimental_result_"$outputLayer"-"$j".txt"
    for i in $(seq 1 $END);
    do
        if [ "$i" = "$END" ]
        then
            python3 src/LSTM_ICS/main.py $finder $filename $outputLayer $test $batchSize $epoch $i >> $path
        else
            python3 src/LSTM_ICS/main.py $finder $filename $outputLayer $test $batchSize $epoch $i >> $path &
        fi
    done
done