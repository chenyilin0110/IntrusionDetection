reset
# set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom horizontal font ",15"
set yrange [0.45 : 0.55]
set ytics 0,0.03 font ",15"

set style line 1\
	linecolor rgb "#49434a"

set style line 2\
	linecolor rgb "#0C3559"
	
set style line 3\
	linecolor rgb "#BF05F2"

set style line 4\
	linecolor rgb "#F22727"
    
set ylabel "Accuracy" font ",17" offset -0.6,0.3
set xtics font ",17"
plot "src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg-21.txt" using 2:xtic(1) with histogram linestyle 1 fillstyle pattern 6 title "DNN",\
"src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg-21.txt" using 3:xtic(1) with histogram linestyle 2 fillstyle pattern 6 title "HC-DNN",\
"src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg-21.txt" using 4:xtic(1) with histogram linestyle 3 fillstyle pattern 6 title "SA-DNN",\
"src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg-21.txt" using 5:xtic(1) with histogram linestyle 4 title "GA-DNN"
set terminal pdf
set output "src/Plot/NSL-KDD-2parameters/5class/5classAccuracy-21.pdf"
replot

#output  ------------------------------------------------------------------------------------------------------------------------
set output
