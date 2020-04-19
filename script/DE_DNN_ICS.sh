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
mid=`expr $END / 2`

# DE_DNN 2 categories
finder="2"
outputLayer="2"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    for i in $(seq 1 $END);
    do
        path="src/DE_DNN_ICS/result/experimental_result_"$outputLayer"-"$j"-"$i".txt"
        if [ "$i" -gt "$mid" ]
        then
            if [ "$i" = "$END" ]
            then
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path
            else
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
            fi            
        else
            CUDA_VISIBLE_DEVICES=0 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
        fi
    done
done

# DE_DNN 3 categories
finder="3"
outputLayer="3"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    for i in $(seq 1 $END);
    do
        path="src/DE_DNN_ICS/result/experimental_result_"$outputLayer"-"$j"-"$i".txt"
        if [ "$i" -gt "$mid" ]
        then
            if [ "$i" = "$END" ]
            then
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path
            else
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
            fi            
        else
            CUDA_VISIBLE_DEVICES=0 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
        fi
    done
done

# DE_DNN multi categories
finder="multi"
outputLayer="41"
for j in $(seq 1 $data);
do
    filename="data"$j".csv"
    for i in $(seq 1 $END);
    do
        path="src/DE_DNN_ICS/result/experimental_result_"$outputLayer"-"$j"-"$i".txt"
        if [ "$i" -gt "$mid" ]
        then
            if [ "$i" = "$END" ]
            then
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path
            else
                CUDA_VISIBLE_DEVICES=1 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
            fi            
        else
            CUDA_VISIBLE_DEVICES=0 python3 src/DE_DNN_ICS/main.py $finder $filename $outputLayer $hiddenLayer $hiddenNeural $test $iteration $epoch $population $F $CR $j >> $path &
        fi
    done
done