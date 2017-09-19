#Create a simulator object.
set ns [new Simulator]

# duration of simulation
set duration 60

set windowSize [lindex $argv 0]
set queueSize 20
set linkDelay [lindex $argv 1]

#Open the NAM trace file
set file1 [open out.nam w]
$ns namtrace-all $file1

# select random seed for NS
ns-random 0

#Open the trace file
set file2 [open outWindow.tr w]
set winfile [open Window.tr w]
$ns trace-all $file2

#Define a 'finish' procedure
proc finish {} {
	global ns file1 file2

	$ns flush-trace
	close $file1
	close $file2
	#exec nam out.nam &
	exit 0
}

#Create 2 nodes
set n0 [$ns node]
set n1 [$ns node]

#Create a link between them
$ns duplex-link $n0 $n1 1Mbps $linkDelay DropTail

$ns queue-limit $n0 $n1 $queueSize
set flink [$ns link $n0 $n1]


#Set flow monitor
set monfile [open WindowMon.tr w]
set fmon [$ns makeflowmon Fid]
$fmon reset

#$fmon attach $monfile
$ns attach-fmon $flink $fmon

#Create a TCP agent and attach it to node n0
set tcp0 [new Agent/TCP]
$tcp0 set window_ $windowSize
$tcp0 set fid_ 1
$tcp0 set packetSize_ 500B
$ns attach-agent $n0 $tcp0

# Create a FTP traffic source and attach it to tcp0
set ftp0 [new Application/FTP]
$ftp0 set packetSize_ 500B

$ftp0 set interval_ 0.01
$ftp0 attach-agent $tcp0

#Create a TCP Sink  agent (a traffic sink) and attach it to node n1
set tcpSink0 [new Agent/TCPSink]
$ns attach-agent $n1 $tcpSink0

#Connect the traffic source with the traffic sink
$ns connect $tcp0 $tcpSink0

#Schedule events for the FTP agent
$ns at 0.5 "$ftp0 start"
#$ns at 9.5 "$ftp0 stop"

proc plotWindow {tcpSource file} {
	global ns windowSize
	set time 0.02
	set now [$ns now]
	set cwnd [$tcpSource set cwnd_]
	if { $cwnd < $windowSize } then {
		puts $file "$now $cwnd"
	} else {

		puts $file "$now $windowSize"
	}
	$ns at [expr $now+$time] "plotWindow $tcpSource $file"
}

proc plotTPut {file} {
	global ns fmon lastpktsd
	set time 1.0
	set now [$ns now]
	# get flow classifier
	set fcl [$fmon classifier]
	# get flow number 1
	set flow [$fcl lookup auto 0 0 1]

	if { $flow !="" } then {
		set drops [$flow set pdrops_]
		set pktsa [$flow set parrivals_]
		set pktsd [$flow set pdepartures_]
		set queue [$flow set pkts_]
		set tput [expr 1.0*($pktsd -$lastpktsd)/$time]
		set avgtput [expr 1.0*$pktsd/($now - 0.5)]
		set lastpktsd $pktsd
		if { $pktsa > 0 } then {
			set droprate [expr 1.0*$drops / $pktsa]
		} else {
			set droprate 0
		}
		puts $file "$now $drops  $droprate $tput $queue $avgtput"
	}

	$ns at [expr $now+$time] "plotTPut $file"
}
set lastpktsd 0

$ns at 0.1 "plotWindow $tcp0 $winfile"
$ns at 0.1 "plotTPut $monfile"

#Call the finish procedure after $duration seconds of simulation time
$ns at $duration "finish"

#Run the simulation
$ns run