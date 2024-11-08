#! /bin/sh
a=$1
if [ -n "$a" ]
then
  for i in `seq 1 $a`
  do
    echo hello world
  done
else
  while [ True ]
  do
    echo hello world
  done
fi
