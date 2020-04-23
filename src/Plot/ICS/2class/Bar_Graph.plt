reset
set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom center horizontal font ",17"
set yrange [0.2 : 0.99]
set ytics 0,0.1 font ",15"

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

set ylabel "Accuracy" font ",17" offset -0.6
set xtics font ",17"
plot \
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-1.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-1.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-2.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-2.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-3.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-3.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-4.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"
set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-4.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-5.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-5.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-6.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-6.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-7.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-7.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-8.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-8.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-9.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-9.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-10.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-10.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-11.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-11.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-12.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-12.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-13.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-13.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-14.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-14.png"
replot

plot \
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 2:xtic(1) with histogram linestyle 1 title "DAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 3:xtic(1) with histogram linestyle 2 title "SNDAE",\
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 4:xtic(1) with histogram linestyle 3 title "DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 5:xtic(1) with histogram linestyle 4 title "DE-DNN",\
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 6:xtic(1) with histogram linestyle 5 title "NaiveBayes",\
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 7:xtic(1) with histogram linestyle 6 title "RandomForest",\
"src/Plot/ICS/2class/ICS_2class_Avg-15.txt" using 8:xtic(1) with histogram linestyle 7 title "SVM"

set terminal png
set output "src/Plot/ICS/2class/2classAccuracy-15.png"
replot

#output  ------------------------------------------------------------------------------------------------------------------------
set output