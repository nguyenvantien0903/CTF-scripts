#!/bin/bash



while :
do
cnt=`ls -laS | grep malfinder | wc -l`
if [[ $cnt -eq 2 ]]
then
	echo "asdasdasdadadasdadasdasdasd"
	file=`ls -laS | grep malfinder | head -n 1 | cut -d " " -f9`
	file1=`ls -laS | grep malfinder | head -n 1 | cut -d " " -f10`
	file2=`ls -laS | grep malfinder | head -n 1 | cut -d " " -f11`
	file3=`ls -laS | grep malfinder | head -n 1 | cut -d " " -f12`
	rm $file || rm $file1 || rm $file2 || rm $file3
fi

output=`file malfinder*`
echo $output

if [[ $output == *"bzip2"* ]]
then
	mv malfinder* malfinder.bz2
	bzip2 -d malfinder.bz2
elif [[ $output == *"Zip archive data"* ]]
then
	mv malfinder* malfinder.zip
	unzip malfinder.zip
elif [[ $output == *"gzip compressed data"* ]]
then
	mv malfinder* malfinder.gz
	gzip -d malfinder.gz
elif [[ $output == *"XZ compressed data"* ]]
then
	mv malfinder* malfinder.xz
	xz -d malfinder.xz
else
  echo "It's there!3"
fi

sleep 0.5
done
