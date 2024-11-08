#! /bin/sh
d=$1
if [ ! \( -e $d \) ]
then
  mkdir $d
fi
(
cd $d
for n in `seq 0 4`
do
  touch file$n.txt
done 
tar cvf files.tar file0.txt file1.txt file2.txt file3.txt file4.txt
mkdir files
mv files.tar files
(
cd files
tar xvf files.tar
)
)

