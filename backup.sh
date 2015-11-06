#!/bin/bash
name=$(date +%F-%T)_loginapp.sqlite
cp /home/localuser/newsite/loginapp.sqlite /home/localuser/newsite/$name
lftp sftp://localuser:team16@studmohamiah-p.cs.ucl.ac.uk  -e "cd Backup; put /home/localuser/newsite/$name; bye"
rm /home/localuser/newsite/$name
echo "Backup complete"
