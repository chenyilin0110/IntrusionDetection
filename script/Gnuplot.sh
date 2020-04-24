#!/bin/bash

# KDD99 2 categories
gnuplot src/Plot/KDD99/2class/Bar_Graph.plt

# KDD99 5 categories
gnuplot src/Plot/KDD99/5class/Bar_Graph.plt

# NSL-KDD 2 categories
gnuplot src/Plot/NSL-KDD/2class/Bar_Graph.plt
gnuplot src/Plot/NSL-KDD/2class/Bar_Graph-21.plt

# NSL-KDD 5 categories
gnuplot src/Plot/NSL-KDD/5class/Bar_Graph.plt
gnuplot src/Plot/NSL-KDD/5class/Bar_Graph-21.plt

# ICS 2 categories
gnuplot src/Plot/ICS/2class/Line.plt
# gnuplot src/Plot/ICS/2class/Bar_Graph.plt

# ICS 3 categories
# gnuplot src/Plot/ICS/3class/Bar_Graph.plt
gnuplot src/Plot/ICS/3class/Line.plt

# ICS multi categories
# gnuplot src/Plot/ICS/multi/Bar_Graph.plt
gnuplot src/Plot/ICS/multi/Line.plt