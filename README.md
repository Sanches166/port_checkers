# Port listeners for server
This repository contains scripts that will help you track scanning and connection attempts to your server and collect all the information in separate files convenient for further analysis.

## Содержание
- [Technologies](#technologies)
- [Start](#start)
- [Description](#description)

## Technologies
- [Python](https://www.python.com/)
- Asyncio
- Socket
- Logging

## Start

### Requirements
Для установки зависимостей, выполните команду:
```py
$ pip install -r requirements.txt
```

### Run
```sh
$ python3 [name_of_file.py]
```

## Description

### Telnet
This script listen most popular ports (PORTS variable) on the server and log user/password in file. User have 5 attempts to try connect to server before disconnect. 

### Converter
This code convert .log file into xlsx table for further analisys with columns: Protocol, Source IP, Source Port, Destination IP, Destination Port, Flags.

### NMAP listener
Code in this file provide opportunity to check if you've been scaned by Nmap. You will see which protocol have been used (UDP/TCP), source IP:PORT, destination IP:PORT and flags ("FIN", "SYN", "RST", "PSH", "ACK", "URG", "CWR", "ECE").

### SSH
This listener logging ssh connection information with time, source IP address, when the user cancels the connection and was disconnected.

## Sources
These scripts were created to conduct research during the course of the diploma. They helped to collect personal statistics of server accesses and to identify the most popular ports to access. 
