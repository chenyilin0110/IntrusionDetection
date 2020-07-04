rm src/Plot/KDD99/2class/KDD99_2class_recall_Avg.txt
rm src/Plot/KDD99/5class/KDD99_5class_recall_Avg.txt
dataset="KDD99"
categories="2"
echo "KDD CUP 99 2 categories" >> src/Plot/KDD99/2class/KDD99_2class_recall_Avg.txt
python3 src/Other/getRecall.py DAE $dataset $categories
python3 src/Other/getRecall.py SNDAE $dataset $categories
python3 src/Other/getRecall.py DNN $dataset $categories
python3 src/Other/getRecall.py DE_DNN $dataset $categories
python3 src/Other/getRecall.py LSTM $dataset $categories
python3 src/Other/getRecall.py DE_LSTM $dataset $categories
python3 src/Other/getRecall.py Naive_Bayes $dataset $categories
python3 src/Other/getRecall.py RandomForest $dataset $categories
python3 src/Other/getRecall.py SVM $dataset $categories
python3 src/Other/getRecall.py KNN $dataset $categories

categories="5"
echo "KDD CUP 99 5 categories" >> src/Plot/KDD99/5class/KDD99_5class_recall_Avg.txt
python3 src/Other/getRecall.py DAE $dataset $categories
python3 src/Other/getRecall.py SNDAE $dataset $categories
python3 src/Other/getRecall.py DNN $dataset $categories
python3 src/Other/getRecall.py DE_DNN $dataset $categories
python3 src/Other/getRecall.py LSTM $dataset $categories
python3 src/Other/getRecall.py DE_LSTM $dataset $categories
python3 src/Other/getRecall.py Naive_Bayes $dataset $categories
python3 src/Other/getRecall.py RandomForest $dataset $categories
python3 src/Other/getRecall.py SVM $dataset $categories
python3 src/Other/getRecall.py KNN $dataset $categories

dataset="NSL-KDD"
categories="2"
python3 src/Other/getRecall.py DAE $dataset $categories
python3 src/Other/getRecall.py SNDAE $dataset $categories
python3 src/Other/getRecall.py DNN $dataset $categories
python3 src/Other/getRecall.py DE_DNN $dataset $categories
python3 src/Other/getRecall.py LSTM $dataset $categories
python3 src/Other/getRecall.py DE_LSTM $dataset $categories
python3 src/Other/getRecall.py Naive_Bayes $dataset $categories
python3 src/Other/getRecall.py RandomForest $dataset $categories
python3 src/Other/getRecall.py SVM $dataset $categories
python3 src/Other/getRecall.py KNN $dataset $categories

categories="5"
python3 src/Other/getRecall.py DAE $dataset $categories
python3 src/Other/getRecall.py SNDAE $dataset $categories
python3 src/Other/getRecall.py DNN $dataset $categories
python3 src/Other/getRecall.py DE_DNN $dataset $categories
python3 src/Other/getRecall.py LSTM $dataset $categories
python3 src/Other/getRecall.py DE_LSTM $dataset $categories
python3 src/Other/getRecall.py Naive_Bayes $dataset $categories
python3 src/Other/getRecall.py RandomForest $dataset $categories
python3 src/Other/getRecall.py SVM $dataset $categories
python3 src/Other/getRecall.py KNN $dataset $categories