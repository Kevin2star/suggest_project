#! /bin/sh
if [ ! \( -n DB.txt \) ]
then
  touch DB.txt
fi
echo $1 $2 >> DB.txt
