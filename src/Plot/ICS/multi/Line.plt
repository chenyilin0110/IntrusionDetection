reset
# set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom horizontal font ",15"
set yrange [0.0 : 0.99]
set ytics 0,0.1 font ",15"

set style line 1 \
  linecolor rgb '#58355E' \
  linetype 1 linewidth 0.8 \
  pointtype 1 pointsize 0.5

set style line 2 \
  linecolor rgb '#E03616' \
  linetype 2 linewidth 0.8 \
  pointtype 2 pointsize 0.5

set style line 3 \
  linecolor rgb '#FFBF00' \
  linetype 3 linewidth 0.8 \
  pointtype 3 pointsize 0.5

set style line 4 \
  linecolor rgb '#50C878' \
  linetype 4 linewidth 0.8 \
  pointtype 4 pointsize 0.5

set style line 5 \
  linecolor rgb '#5998C5' \
  linetype 5 linewidth 0.8 \
  pointtype 5 pointsize 0.5

set style line 6 \
  linecolor rgb '#EDAFB8' \
  linetype 6 linewidth 0.8 \
  pointtype 6 pointsize 0.5

set style line 7 \
  linecolor rgb '#E07B42' \
  linetype 7 linewidth 0.8 \
  pointtype 7 pointsize 0.5

set style line 8 \
  linecolor rgb '#008080' \
  linetype 8 linewidth 0.8 \
  pointtype 8 pointsize 0.5

set style line 9 \
  linecolor rgb '#B399FF' \
  linetype 10 linewidth 0.8 \
  pointtype 10 pointsize 0.5

set ylabel "Accuracy" font ",17"
set xtics font ",17"
plot \
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 2:xtic(1) with linespoints linestyle 1 title "DAE",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 3:xtic(1) with linespoints linestyle 2 title "SNDAE",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 4:xtic(1) with linespoints linestyle 3 title "DNN",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 5:xtic(1) with linespoints linestyle 4 title "DE-DNN",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 6:xtic(1) with linespoints linestyle 5 title "LSTM",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 7:xtic(1) with linespoints linestyle 6 title "DE-LSTM",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 8:xtic(1) with linespoints linestyle 7 title "NaiveBayes",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 9:xtic(1) with linespoints linestyle 8 title "RandomForest",\
"src/Plot/ICS/multi/ICS_multi_Avg.txt" using 10:xtic(1) with linespoints linestyle 9 title "SVM"

set terminal pdf
set output "src/Plot/ICS/multi/multiAccuracy.pdf"
replot

#output  ------------------------------------------------------------------------------------------------------------------------
set output