reset
# set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom horizontal font ",15"
set yrange [0.44 : 0.73]
set ytics 0,0.03 font ",15"

set style line 1\
	linecolor rgb "#49434a"

set style line 2\
	linecolor rgb "#0C3559"
	
set style line 3\
	linecolor rgb "#BF05F2"

set style line 4\
	linecolor rgb "#F22727"

set style line 5\
	linecolor rgb "#8E2800"

set style line 6\
	linecolor rgb "#034001"

set style line 7\
	linecolor rgb "#354e94"

set style line 8\
	linecolor rgb "#F26D9E"

set style line 9\
	linecolor rgb "#F2845C"

set style line 10\
	linecolor rgb "#7ED955"

set style line 11\
	linecolor rgb "#8D27F2"

set style line 12\
	linecolor rgb "#F2CD88"

set style line 13\
	linecolor rgb "#D9725B"

set ylabel "Recall" font ",17" offset -0.6
set xtics font ",17"
set terminal pdf
set output "src/Plot/NSL-KDD/2class/2classRecall-21.pdf"

plot \
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 8:xtic(1) with histogram linestyle 7 fillstyle pattern 6 title "NaiveBayes",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 4:xtic(1) with histogram linestyle 3 fillstyle pattern 6 title "DNN",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 2:xtic(1) with histogram linestyle 1 fillstyle pattern 6 title "DAE",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 10:xtic(1) with histogram linestyle 9 fillstyle pattern 6 title "SVM",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 3:xtic(1) with histogram linestyle 2 fillstyle pattern 6 title "SNDAE",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 11:xtic(1) with histogram linestyle 10 fillstyle pattern 6 title "KNN",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 6:xtic(1) with histogram linestyle 5 fillstyle pattern 6 title "LSTM",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 9:xtic(1) with histogram linestyle 8 fillstyle pattern 6 title "RandomForest",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/NSL-KDD/2class/NSL-KDD_2class_recall_Avg-21.txt" using 7:xtic(1) with histogram linestyle 6 title "DE-LSTM"