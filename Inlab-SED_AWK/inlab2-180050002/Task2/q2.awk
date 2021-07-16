BEGIN { print "Value     SensorNumber";
    OFS="\t"; RS="!"; FS=","}

{print $1,$2 ;}
END{}
	       
