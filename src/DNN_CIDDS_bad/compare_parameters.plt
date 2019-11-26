reset
set title "Deep Neural Network"
set style data histogram
#histogram 寬度
set boxwidth 0.8 relative
set xlabel ' ' offset 0, -1.5 font "Times New Roman,16"
set ylabel 'Accuracy' font "Times New Roman,10"
set style histogram clustered gap 0.5 title offset 0, 1 font "Times New Roman,16"
set grid
set key off
set tics font "Times New Roman,12"
#填滿類型
set style fill solid
#邊線類型
set style fill border 0


plot \
newhistogram "neurons", \
'result/neurons_result.txt' using 2:xtic(1) linecolor rgb "#D9E962", \
newhistogram "hidden layer", \
'result/hiddenlayer_result.txt' using 2:xtic(1) linecolor rgb "#3D80D9"
set terminal png
set output "compare parameters.png"
replot
set output