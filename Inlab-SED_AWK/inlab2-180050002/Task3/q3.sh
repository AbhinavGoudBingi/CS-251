#!/bin/bash

sed -n '1 c\
Team        Played        Wins        Tied        Points' $1

awk 'BEGIN{ FS="\t"
            OFS="\t"
            }
       /[0-9]/{print $1,$2,$3,$4,$3*4+$4*2 }
           END{}' $1
