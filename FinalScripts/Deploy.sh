#!/bin/bash
cd ~/
scp bash.sh localuser@studtphung-p.cs.ucl.ac.uk:
ssh -t localuser@studtphung-p.cs.ucl.ac.uk "sudo bash bash.sh"
