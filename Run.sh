#!/bin/bash
sh Run/Run_HC_LSTM_KDD.sh >> src/HC_LSTM_KDD99/result/experimental_result_2.txt &
sh Run/Run_DE_DNN_KDD.sh >> src/DE_DNN_KDD99/result/experimental_result_2.txt
sh Run/Run_DAE_KDD.sh >> src/DAE_KDD99/result/experimental_result_2.txt &
sh Run/Run_SNDAE_KDD.sh >> src/SNDAE_KDD99/result/experimental_result_2.txt