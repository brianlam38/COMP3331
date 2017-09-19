set xlabel "time [s]"
set ylabel "Throughput [packets/sec]"
set key bel
plot  "WindowMon.tr" u ($1):($4) t "Instant Throughput" w lp, "WindowMon.tr" u ($1):($6) t "Average Throughput" w lp
pause -1
