#! /bin/sh
d=$1
(
cd $d
for n in `seq 0 4`
do
  touch file$n.txt
  mkdir file$n
  (
  cd file$n
  ln -s file$n.txt file$n.txt
  )
done
)
