#!/bin/bash
ssh localuser@studmohamiah-p.cs.ucl.ac.uk ./Recover.sh
cd /home/localuser/Recovery/
file=$(ls -t |head -n1)
cp $file /home/localuser/newsite/loginapp.sqlite
echo "Database has been restored"
