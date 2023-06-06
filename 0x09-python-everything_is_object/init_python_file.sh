#!/bin/bash

filename=$1
touch $filename
chmod +x $filename
echo "#!/usr/bin/python3" > $filename
vim $filename
