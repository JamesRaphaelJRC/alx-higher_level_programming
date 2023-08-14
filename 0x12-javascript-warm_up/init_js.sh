#!/bin/bash

# - This script creates a file, change its permission, writes into it and opens it in vim automatically

if [ $# -eq 0 ]; then
	echo "No filename provided!"
	exit 1
fi

filename=$1
touch "$filename"
chmod +x "$filename"
echo "#!/usr/bin/node" > "$filename"
vim "$filename"
