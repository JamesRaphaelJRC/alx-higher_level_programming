#!/bin/bash
# Displays the HTTP methods a server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
