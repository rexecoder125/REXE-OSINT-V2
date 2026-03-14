#!/bin/bash

clear
echo "Installing CODER OSINT TOOL v2..."

pkg update -y
pkg upgrade -y

pkg install python -y
pkg install git -y
pkg install curl -y
pkg install dnsutils -y

pip install requests
pip install colorama
pip install dnspython

chmod +x rexe.py

echo ""
echo "Installation Complete!"
echo ""
echo "Run Tool Using:"
echo "python rexe.py"
