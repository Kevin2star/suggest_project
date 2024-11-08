#! /bin/sh
weight=$1
height=$2
mheight=`echo "scale=2; $height / 100" | bc -l`
sqheight=`echo "scale=4; $mheight * $mheight" | bc -l`
bmi=`echo "scale=4; $weight / $sqheight" | bc -l`
if [ $(echo "scale=1; $bmi >= 23" | bc) -ne 0 ]
then
  echo "과체중입니다."
else
  if [ $(echo "scale=1; $bmi < 18.5" | bc) -ne 0 ]
  then
    echo "저체중입니다."
  else
    echo "정상체중입니다."
  fi
fi
