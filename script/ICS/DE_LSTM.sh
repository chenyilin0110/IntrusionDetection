#!/bin/bash
hiddenLayer=1
test=20
batchSize=256
epoch=100
iteration=40
population=20
F=0.5
CR=0.3

data=15
END=4
mid=`expr $END / 2`

# DE_LSTM 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    for i in $(seq 1 $END);
    do
        path="src/DE_LSTM_ICS/result/experimental_result_"$outputLayer"-"$j"-"$i".txt"
        if [ "$i" -gt "$mid" ]
        then
            if [ "$i" = "$END" ]
            then
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path
            else
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path &
            fi
        else
            CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path &
        fi
    done
done

# DE_LSTM 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    for i in $(seq 1 $END);
    do
        path="src/DE_LSTM_ICS/result/experimental_result_"$outputLayer"-"$j"-"$i".txt"
        if [ "$i" -gt "$mid" ]
        then
            if [ "$i" = "$END" ]
            then
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path
            else
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path &
            fi
        else
            CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path &
        fi
    done
done

# DE_LSTM multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    for i in $(seq 1 $END);
    do
        path="src/DE_LSTM_ICS/result/experimental_result_"$outputLayer"-"$j"-"$i".txt"
        if [ "$i" -gt "$mid" ]
        then
            if [ "$i" = "$END" ]
            then
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path
            else
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path &
            fi
        else
            CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_ICS/main.py $finder $filename $hiddenLayer $outputLayer $test $batchSize $epoch $iteration $population $F $CR $i >> $path &
        fi
    done
done