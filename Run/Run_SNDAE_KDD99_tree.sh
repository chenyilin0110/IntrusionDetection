#!/bin/bash
train="train"
test="test"
outputLayer="5"
learning_rate="0.01"
END=10
tree="5"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="20"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="30"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="40"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="50"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="60"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="70"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="80"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="90"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="100"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="110"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="120"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="130"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="140"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="150"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="160"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="170"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="180"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="190"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done

tree="200"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_KDD99/main.py $train $test $outputLayer $tree $learning_rate
done