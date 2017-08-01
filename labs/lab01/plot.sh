#!/bin/sh


plot=""
plot2=""

outname=`echo $1 | sed -e "s/-p/ p/" | awk '{print $1}'`
outavg=$outname\_avg.txt
echo $outname

# cycle through all filenames
until [ -z "$1" ]
do
  echo "processing $1"

  # grep only for the lines with ping data,
  # plot the field's we're interested in and
  # write to temp file
  MIN=`grep min $1 | sed -e "s/\// /g" | awk '{print $7}'`
  AVG=`grep avg $1 | sed -e "s/\// /g" | awk '{print $8}'`
  PSIZE=`grep icmp_req $1 | head -1 | awk '{print int($1)+20}'`
  echo "$PSIZE $AVG $MIN"
  echo "$PSIZE $AVG $MIN" >> avg.tmp
  grep icmp_req $1 | sed -e "s/=/ /g" | awk '{if (NF == 12) print $7 " " $11 " " $1; else print $6 " " $10 " " $1}' > $1.tmp

  #compose plot command for gnuplot
  plot="$plot \"$1.tmp\" u 1:2 not w l"
  plot2="$plot2 \"$1.tmp\" u 3:2 not w p"

  shift
  if [ -n "$1" ] ; then # no , after last file
      plot="$plot,"
      plot2="$plot2,"
  fi
done
sort -n avg.tmp > $outavg

# plot the temp files with gnuplot
echo "set term postscript color; set output \"$outname\_delay.ps\"; set xlabel \"Packet Number\"; set ylabel \"Delay (ms)\"; plot $plot" | gnuplot - > /dev/null 2> /dev/null
echo "ps2pdf "$outname"_delay.ps"
ps2pdf "$outname"_delay.ps

echo "set term postscript color; set output \"$outname\_scatter.ps\"; set xlabel \"Packet Size (bytes)\"; set ylabel \"Delay (ms)\";  plot $plot2, \"$outavg\" t \"avg\" w l -1 " | gnuplot - > /dev/null 2> /dev/null 
echo "ps2pdf "$outname"_scatter.ps"
ps2pdf "$outname"_scatter.ps

# delete temp files
rm -f *.tmp
