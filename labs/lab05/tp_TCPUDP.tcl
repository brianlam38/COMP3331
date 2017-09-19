#Create a simulator object.
set ns [new Simulator]

$ns color 0 Blue
$ns color 1 Red

set duration 10; # duration of simulation

set windowSize 50
set queueSize 100
set linkCapacity [lindex $argv 0]

#Open the NAM trace file
set file1 [open out.nam w]
$ns namtrace-all $file1

#Open log files
set monfile0 [open TCPUDPMon0.tr w]
set monfile1 [open TCPUDPMon1.tr w]

# select random seed for NS
ns-random 0

#Open the trace file
set file2 [open outWindow.tr w]
set winfile [open Window.tr w]
$ns trace-all $file2

#Define a 'finish' procedure
proc finish {} {
        global ns file1 file2 monfile0 monfile1
        $ns flush-trace
        close $file1
        close $file2
        close $monfile0
        close $monfile1
        exec nam out.nam &
        exit 0
}

#Create 2 nodes
set n0 [$ns node]
set n1 [$ns node]

#Create a link between them
$ns duplex-link $n0 $n1 $linkCapacity 100ms DropTail

$ns queue-limit $n0 $n1 $queueSize
set flink [$ns link $n0 $n1]

#Set flow monitor
set fmon [$ns makeflowmon Fid]
$fmon reset


$ns attach-fmon $flink $fmon


#Create a TCP agent and attach it to node n0
set tcp0 [new Agent/TCP/Sack1]
$tcp0 set window_ $windowSize
$tcp0 set fid_ 0
$ns attach-agent $n0 $tcp0

#Create a UDP agent and attach it to node n0
set udp0 [new Agent/UDP]
$udp0 set fid_ 1
$ns attach-agent $n0 $udp0

# Create a FTP traffic source and attach it to tcp
set ftp0 [new Application/FTP]
$ftp0 set packetSize_ 500
$ftp0 set interval_ 0.001
$ftp0 attach-agent $tcp0

# Create a CBR traffic source and attach it to udp
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.001
$cbr0 attach-agent $udp0

#Create a TCP Sink  agent (a TCP traffic sink) and attach it to node n1
set tcpSink0 [new Agent/TCPSink/Sack1]
$ns attach-agent $n1 $tcpSink0

#Create a null  agent (a UDP traffic sink) and attach it to node n1
set null0 [new Agent/Null]
$ns attach-agent $n1 $null0

#Connect the traffic sources with the traffic sinks
$ns connect $tcp0 $tcpSink0
$ns connect $udp0 $null0

#Schedule events for the FTP agent
$ns at 0.5 "$ftp0 start"
$ns at 0.5 "$cbr0 start"

proc plotTPut {n file} {
    global ns fmon lastpktsd
    set time 0.1
    set now [$ns now]
    # get flow classifier
    set fcl [$fmon classifier]
    # get flow number n
    set flow [$fcl lookup auto 0 0 $n]

    if { $flow !="" } then {
    set drops [$flow set pdrops_]
    set pktsa [$flow set parrivals_]
    set pktsd [$flow set pdepartures_]
    set queue [$flow set pkts_]
    set tput [expr 1.0*($pktsd - $lastpktsd($n))/$time]
    set lastpktsd($n) $pktsd
    if { $pktsa > 0 } then {
        set droprate [expr 1.0*$drops / $pktsa]
    } else {
        set droprate 0
    }
    puts $file "$now $droprate $tput $drops $pktsd"
    }
    $ns at [expr $now+$time] "plotTPut $n $file"
}
set lastpktsd(0) 0
set lastpktsd(1) 0

$ns at 0.1 "plotTPut 0 $monfile0"
$ns at 0.1 "plotTPut 1 $monfile1"

#Call the finish procedure after $duration seconds of simulation time
$ns at $duration "finish"

#Run the simulation
$ns run