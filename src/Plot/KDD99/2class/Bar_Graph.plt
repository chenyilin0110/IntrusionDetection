reset
set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom center horizontal font ",17"
set yrange [0.69 : 0.94]
set ytics 0,0.02 font ",15"

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
    
set ylabel "Accuracy" font ",17" offset -0.6,0.3
set xtics font ",17"
plot "src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 2:xtic(1) with histogram linestyle 1 title "DNN",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 3:xtic(1) with histogram linestyle 2 title "HC-DNN",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 4:xtic(1) with histogram linestyle 3 title "DE-DNN",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 5:xtic(1) with histogram linestyle 4 title "LSTM",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 6:xtic(1) with histogram linestyle 5 title "HC-LSTM",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 7:xtic(1) with histogram linestyle 6 title "DE-LSTM",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 8:xtic(1) with histogram linestyle 7 title "DAE",\
"src/Plot/KDD99/2class/KDD99_2class_Avg.txt" using 9:xtic(1) with histogram linestyle 8 title "SNDAE"
set terminal png
set output "src/Plot/KDD99/2class/2classAccuracy.png"
replot

#output  ------------------------------------------------------------------------------------------------------------------------
set output
