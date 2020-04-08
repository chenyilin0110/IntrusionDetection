#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="5"
epoch="100"

END=10
learning_rate="0.01"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.02"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.03"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.04"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.05"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.06"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.07"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.08"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.09"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.1"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.11"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.12"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.13"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.14"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.15"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.16"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.17"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.18"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.19"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done

learning_rate="0.2"
for i in $(seq 1 $END);
do
    python3 src/DAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $epoch $learning_rate
done