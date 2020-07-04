reset
set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom center horizontal font ",17"
set yrange [0.68 : 0.93]
set ytics 0,0.03 font ",15"

set style line 1\
	linecolor rgb "#49434a"

set style line 2\
	linecolor rgb "#a5cdd4"
	
set style line 3\
	linecolor rgb "#ffea75"

set style line 4\
	linecolor rgb "#F22727"

set style line 5\
	linecolor rgb "#dfc3e6"

set style line 6\
	linecolor rgb "#034001"

set style line 7\
	linecolor rgb "#354e94"

set style line 8\
	linecolor rgb "#F26D9E"

set style line 9\
	linecolor rgb "#85E7F2"

set style line 10\
	linecolor rgb "#7ED955"

set style line 11\
	linecolor rgb "#8D27F2"

set style line 12\
	linecolor rgb "#F2CD88"

set style line 13\
	linecolor rgb "#D9725B"
    
set ylabel "Precision" font ",17" offset -0.6,0.3
set xtics font ",17"
set terminal png
set output "src/Plot/KDD99/2class/2classPrecision.png"

plot \
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 8:xtic(1) with histogram linestyle 7 title "Naive-Bayes",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 5:xtic(1) with histogram linestyle 4 fillstyle pattern 6 title "DE-DNN",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 10:xtic(1) with histogram linestyle 9 title "SVM",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 6:xtic(1) with histogram linestyle 5 title "LSTM",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 11:xtic(1) with histogram linestyle 10 title "KNN",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 9:xtic(1) with histogram linestyle 8 title "Random-Forest",\
"src/Plot/KDD99/2class/KDD99_2class_precision_Avg.txt" using 7:xtic(1) with histogram linestyle 6 fillstyle pattern 6 title "DE-LSTM"