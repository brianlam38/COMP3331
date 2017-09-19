#Create a simulator object.
set ns [new Simulator]

set nodeNb 5
set duration [expr 40.0*$nodeNb]; # duration of simulation
set queueSize 50

#Open the NAM trace file
set file1 [open out.nam w]
$ns namtrace-all $file1

# select random seed for NS
ns-random 0

#Open the trace file
set file2 [open outFairness.tr w]
$ns trace-all $file2

#Open log files
set winfile [open fairnessWin.tr w]
for {set i 1} {$i<=$nodeNb} { incr i } {
    set monfile($i) [open fairnessMon$i.tr w]
}
#Define a 'finish' procedure
proc finish {} {
        global ns file1 file2
        $ns flush-trace
        close $file1
        close $file2
#        exec nam out.nam &
        exit 0
}

#######################
# defining the topology
#######################

# Create Intermediate and destination node
set N1 [$ns node]
set N2 [$ns node]
$ns duplex-link $N1 $N2 1Mb 10ms RED
$ns queue-limit $N1 $N2 $queueSize

#Create n  nodes
for {set i 1} {$i<=$nodeNb} { incr i } {
    set S($i) [$ns node]
    set D($i) [$ns node]
    #create duplex links
    $ns duplex-link $S($i) $N1 1Mb 10ms DropTail
    $ns queue-limit $S($i) $N1 $queueSize
    #set flink($i) [$ns link $S($i) $N1]

    $ns duplex-link $N2 $D($i) 1Mb 10ms DropTail
    $ns queue-limit $N2 $D($i) $queueSize
    set flink($i) [$ns link $N2 $D($i)]


    #Set flow monitors
    set fmon($i) [$ns makeflowmon Fid]
    $fmon($i) reset
    $ns attach-fmon $flink($i) $fmon($i)

    #Create a TCP agent and attach it to node Si
    set tcp($i) [new Agent/TCP/Sack1]
    $tcp($i) set fid_ $i
    $ns attach-agent $S($i) $tcp($i)

    #Create a TCP sink and attach it to node Di
    set tcpSink($i) [new Agent/TCPSink/Sack1]
    $ns attach-agent $D($i) $tcpSink($i)

    # Create a FTP traffic source and attach it to tcp0
    set ftp($i) [new Application/FTP]
    $ftp($i) set packetSize_ 1500
    $ftp($i) set interval_ 0.001
    $ftp($i) attach-agent $tcp($i)

    #Connect the traffic sources with the traffic sink
    $ns connect $tcp($i) $tcpSink($i)



}

#Schedule events for the FTP agent
for {set j 1} {$j<=$nodeNb} { incr j } {
    $ns at [expr 5.0*($j - 1)] "$ftp($j) start"
}

proc plotWindow {n tcpSource file} {
    global ns windowSize
    set time 0.02
    set now [$ns now]
    set cwnd [$tcpSource set cwnd_]
    if { $cwnd < $windowSize } then {
    puts $file "$now $cwnd"
    } else {
    puts $file "$n $now $windowSize"
    }
    $ns at [expr $now+$time] "plotWindow $n $tcpSource $file"
}

proc plotTPut {n flowmon file} {
    global ns lastpktsd
    set time 5
    set now [$ns now]
    # get flow classifier
    set fcl [$flowmon classifier]
    # get flow number n
    set flow [$fcl lookup auto 0 0 $n]

    if { $flow !="" } then {
    set drops [$flow set pdrops_]
    set pktsa [$flow set parrivals_]
    set pktsd [$flow set pdepartures_]
    set queue [$flow set pkts_]
    set tput [expr 1.0*($pktsd -$lastpktsd($n))/$time]
    set lastpktsd($n) $pktsd
    if { $pktsa > 0 } then {
        set droprate [expr 1.0*$drops / $pktsa]
    } else {
        set droprate 0
    }
    # Writes the output file with
    # time | packets arrived | packets delivered | drop_rate | throughput
    puts $file "$now $pktsd $tput"
    }
    $ns at [expr $now+$time] "plotTPut $n $flowmon $file"
}

#Initialize last packets departed
for {set k 1} {$k<=$nodeNb} { incr k } {
    set lastpktsd($k) 0
}
for {set k 1} {$k<=$nodeNb} { incr k } {
    $ns at 0.1 "plotTPut $k $fmon($k) $monfile($k)"
}

#Call the finish procedure after $duration seconds of simulation time
$ns at $duration "finish"

#Run the simulation
$ns run