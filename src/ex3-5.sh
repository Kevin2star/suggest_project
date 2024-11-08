#! /bin/sh
execute ()
{
  echo 함수 안으로 들어 왔음
  if [ -n "$a" ]
  then
    ls $a
  else
    ls
  fi
}
echo 프로그램을 시작합니다.
a=$1
execute $a
echo 프로그램을 종료합니다.
