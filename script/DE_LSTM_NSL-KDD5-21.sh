#!/bin/bash
train="train"
test="test-21"
hiddenLayer="1"
outputLayer="5"
batchSize="10000"
iteration="40"
epoch="80"
population="20"
name="-21"

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0101-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.1 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0101-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.1 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0103-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.3 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0103-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.3 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0105-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.5 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0105-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.5 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0107-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.7 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0107-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.7 $name 2 >> $path

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0109-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.9 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0109-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.1 0.9 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0301-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.1 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0301-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.1 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0303-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.3 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0303-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.3 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0305-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.5 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0305-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.5 $name 2 >> $path

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0307-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.7 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0307-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.7 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0309-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.9 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0309-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.3 0.9 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0501-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.1 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0501-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.1 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0503-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.3 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0503-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.3 $name 2 >> $path

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0505-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.5 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0505-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.5 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0507-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.7 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0507-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.7 $name 2 >> $path

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0509-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.9 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0509-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.5 0.9 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0701-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.1 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0701-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.1 $name 2 >> $path

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0703-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.3 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0703-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.3 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0705-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.5 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0705-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.5 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0707-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.7 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0707-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.7 $name 2 >> $path

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0709-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.9 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0709-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.7 0.9 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0901-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.1 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0901-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.1 $name 2 >> $path &

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0903-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.3 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0903-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.3 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0905-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.5 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0905-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.5 $name 2 >> $path

path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0907-1.txt"
CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.7 $name 1 >> $path &
path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0907-2.txt"
CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.7 $name 2 >> $path &

# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0909-1.txt"
# CUDA_VISIBLE_DEVICES=1 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.9 $name 1 >> $path &
# path="src/DE_LSTM_NSL-KDD/result/parameters/DE_LSTM_"$outputLayer"0909-2.txt"
# CUDA_VISIBLE_DEVICES=0 python3 src/DE_LSTM_NSL-KDD/main.py $train $test $hiddenLayer $outputLayer $batchSize $iteration $epoch $population 0.9 0.9 $name 2 >> $path &