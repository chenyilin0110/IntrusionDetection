reset
# set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom horizontal font ",15"
set yrange [0.52 : 0.70]
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

set ylabel "Accuracy" font ",17" offset -0.6,0.3
set xtics font ",17"
plot "src/Plot/NSL-KDD-2parameters/2class/NSL-KDD-2parameters_2class_Avg-21.txt" using 2:xtic(1) with histogram linestyle 1 title "DNN",\
"src/Plot/NSL-KDD-2parameters/2class/NSL-KDD-2parameters_2class_Avg-21.txt" using 3:xtic(1) with histogram linestyle 2 title "HC-DNN",\
"src/Plot/NSL-KDD-2parameters/2class/NSL-KDD-2parameters_2class_Avg-21.txt" using 4:xtic(1) with histogram linestyle 3 title "SA-DNN",\
"src/Plot/NSL-KDD-2parameters/2class/NSL-KDD-2parameters_2class_Avg-21.txt" using 5:xtic(1) with histogram linestyle 4 title "GA-DNN",\
"src/Plot/NSL-KDD-2parameters/2class/NSL-KDD-2parameters_2class_Avg-21.txt" using 6:xtic(1) with histogram linestyle 5 title "PSO-Optimizer"

set terminal pdf
set output "src/Plot/NSL-KDD-2parameters/2class/2classAccuracy-21.pdf"
replot

#output  ------------------------------------------------------------------------------------------------------------------------
set output
