set xlabel "time [s]"
set ylabel "Throughput [packets/s]"
set key bel
plot "TCPUDPMon0.tr" u ($1):($3) t "TCP" w lp lt rgb "blue", "TCPUDPMon1.tr" u ($1):($3) t "UDP" w lp lt rgb "red"


set term png
set output "TCPUDP_pps.png" 
replot
pause -1
