#!/bin/bash
cd /home/localuser/Backup/
file=$(ls -t |head -n1)
echo $file
cp $file ../$file
cd ..
newfile=${file:0:10}
mv $file $newfile
scp "$newfile" localuser@studvm74-p.cs.ucl.ac.uk:/home/localuser/Recovery
rm $newfile
echo done
