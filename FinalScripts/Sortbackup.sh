#!/bin/bash
name=$(date +%Y-%m-%d -d "yesterday")
mkdir /home/localuser/Backup/$name
mv /home/localuser/Backup/$name*.sqlite /home/localuser/Backup/$name/
toDelete=$(date +%Y-%m-%d -d "7 days ago")
cd /home/localuser/Backup
cd $name
rm *
cd ..
rmdir $name
