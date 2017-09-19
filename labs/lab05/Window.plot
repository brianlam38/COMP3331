set xlabel "time [s]"
set ylabel "Window size"
set key bel
plot "Window.tr" t "TCP Window size" w lp, "WindowMon.tr" u ($1):($5) t "Number of packets in queue" w lp
pause -1
