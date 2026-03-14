#!/bin/bash

clear
echo "Installing REXE OSINT v2"

pkg update -y
pkg install python -y
pkg install git -y

pip install -r requirements.txt

chmod +x rexe.py

echo "Run tool:"
echo "python rexe.py"
