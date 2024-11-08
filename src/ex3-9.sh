#! /bin/sh
cnt=0
cat DB.txt | while read line
do
  if [ ${cnt} -eq 0 ]
  then
    cnt=1
    continue
  else
    inp=$1
    case "$line" in
      *"$inp"*)
        echo "$line";;
    esac
  fi
done
