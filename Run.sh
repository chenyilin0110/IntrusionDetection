#!/bin/bash
sh Run/Run_DNN_KDD.sh >> src/DNN_KDD99/result/experimental_result.txt &
sh Run/Run_HC_DNN_KDD.sh >> src/HC_DNN_KDD99/result/experimental_result.txt
sh Run/Run_LSTM_KDD.sh >> src/LSTM_KDD99/result/experimental_result.txt &
sh Run/Run_HC_LSTM_KDD.sh >> src/HC_LSTM_KDD99/result/experimental_result.txt