#!/bin/bash

if [ $# -eq 0 ]; then
	echo "No filename provided!"
	exit 1
fi

filename=$1
touch "$filename"
chmod +x "$filename"
echo "#!/usr/bin/node" > "$filename"
vim "$filename"
