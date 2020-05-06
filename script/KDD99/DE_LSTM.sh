#!/bin/bash
train="train"
test="test"
hiddenLayer="1"
batchSize="2560"
iteration="40"
epoch="100"
population="20"
F="0.5"
CR="0.3"

END=3
mid=`expr $END / 2`

# DE_LSTM_KDD 2 categories
outputLayer="2"
for i in $(seq 1 $END);
do
    path="src/DE_LSTM_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" -gt "$mid" ]
    then
        if [ "$i" = "$END" ]
        then
            CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $i >> $path
        else
            CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $i >> $path &
        fi
    else
        CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $i >> $path &
    fi
done

# DE_LSTM_KDD 5 categories
outputLayer="5"
for i in $(seq 1 $END);
do
    path="src/DE_LSTM_KDD99/result/experimental_result_"$outputLayer"-"$i".txt"
    if [ "$i" -gt "$mid" ]
    then
        if [ "$i" = "$END" ]
        then
            CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $i >> $path
        else
            CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $i >> $path &
        fi
    else
        CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_KDD99/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population $F $CR $i >> $path &
    fi
done