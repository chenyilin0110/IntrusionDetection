#!/bin/bash
train="test"
test="train"
outputLayer="5"
epoch="100"
END=10

hiddenLayer="1"
hiddenNeural="80"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="2"
hiddenNeural="80"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="3"
hiddenNeural="80"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="4"
hiddenNeural="80"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="5"
hiddenNeural="80"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="1"
hiddenNeural="90"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="2"
hiddenNeural="90"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="3"
hiddenNeural="90"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="4"
hiddenNeural="90"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="5"
hiddenNeural="90"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="1"
hiddenNeural="100"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="2"
hiddenNeural="100"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="3"
hiddenNeural="100"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="4"
hiddenNeural="100"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done

hiddenLayer="5"
hiddenNeural="100"
for i in $(seq 1 $END);
do
    python3 src/DNN_CIDDS_bad/main.py $train $test $outputLayer $hiddenLayer $hiddenNeural $epoch
done