#!/usr/bin/bash
echo '[Unit]
Description='$1'
Requires=network.target
After=network.target

[Service]
User='$2'
Group='$3'
Type=simple
ExecStart=/usr/bin/python3 "'$4'" "'$5'" "'$6'" "'$7'"
Restart=always
RestartSec='$8'

[Install]
WantedBy=multi-user.target'
