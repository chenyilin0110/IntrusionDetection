#!/bin/bash
train="train"
test="test"
test_21="test-21"
outputLayer="5"

END=10
tree="10"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="20"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="30"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="40"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="50"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="60"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="70"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="80"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="90"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="100"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="110"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="120"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="130"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="140"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="150"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="160"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="170"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="180"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="190"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done

tree="200"
for i in $(seq 1 $END);
do
    python3 src/SNDAE_NSL-KDD/main.py $train $test $test_21 $outputLayer $tree
done