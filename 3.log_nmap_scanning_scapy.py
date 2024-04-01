import logging
from scapy.all import *

logging.basicConfig(filename='network.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def check_flags(flags):
    flag_names = ["FIN", "SYN", "RST", "PSH", "ACK", "URG", "CWR", "ECE"]
    set_flags = []
    for i in range(6):
        if flags & (1 << i):
            set_flags.append(f'"{flag_names[i]}"')
    return ', '.join(set_flags)


def process_packet(packet):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags
        logging.info('{' +
                        '"proto": "TCP", '
                        '"src": '  +
                            '{' +
                                f'"ip": "{src_ip}", ' +
                                f'"port": {src_port} ' +
                            '}, ' +
                        '"dst": ' +
                            '{' +
                                f'"ip": "{dst_ip}", ' +
                                f'"port": {dst_port} ' +
                            '}, ' +
                        f'"flags": [{check_flags(flags)}]' +
                    '}')
    elif packet.haslayer(UDP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        logging.info('{' +
                        '"proto": "UDP", '
                        '"src": '  +
                            '{' +
                                f'"ip": "{src_ip}", ' +
                                f'"port": {src_port} ' +
                            '}, ' +
                        '"dst": ' +
                            '{' +
                                f'"ip": "{dst_ip}", ' +
                                f'"port": {dst_port} ' +
                            '}, ' +
                    '}')


sniff(filter="dst 192.168.1.7", prn=process_packet)