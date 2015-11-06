#!/bin/bash
name=$(date +%F-%T)_loginapp.sqlite
cp loginapp.sqlite $name
lftp sftp://localuser:team16@studmohamiah-p.cs.ucl.ac.uk  -e "cd Backup; put $name; bye"
rm $name
echo "Backup complete"
