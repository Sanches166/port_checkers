import socket
import logging
import threading

HOST = '192.168.1.3'  # Bind the socket to any available interface
PORTS =  [
    80, 443, 53, 22, 21, 110, 143, 23, 465, 587, 993, 995, 3306, 3389, 8080,
    1723, 111, 5900, 8888, 199, 1720, 69, 514, 1433, 5901, 1024, 1194, 5432, 5902,
    1025, 1026, 1027, 1028, 1029, 1110, 1434, 2000, 2001, 2121, 3986, 4899, 6000,
    6001, 6646, 8000, 8008, 8443, 10000, 50000, 50070, 50090, 11211, 27017, 28017,
    32768, 49152, 49153, 49154, 49155, 49156, 49157, 50030, 50060, 61616, 8083,
    9000, 16010, 16030, 18080, 2222, 54321, 27018, 27019, 28018, 28019, 48080, 50010,
    50020, 50470, 54328, 54329, 56168, 61120, 61750
]
  # Specify the list of ports to listen on
MAX_LOGIN_ATTEMPTS = 5 # Maximum number of login attempts

# Set up logging
logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def accept_connection(sock):
    while True:
        conn, addr = sock.accept()
        logging.info(f"{addr} - {sock.getsockname()[1]}")
        for i in range(MAX_LOGIN_ATTEMPTS):
            # Send message requesting credentials
            conn.sendall('Login: '.encode('utf-8'))
            username = conn.recv(1024).decode().strip()

            conn.sendall('Password: '.encode('utf-8'))
            password = conn.recv(1024).decode().strip()

            logging.warning(f"Invalid credentials from {addr} on port {sock.getsockname()[1]}")
            logging.info(f"Creds->{username}:{password} on port {sock.getsockname()[1]}")
            conn.sendall('Invalid credentials. Please try again.\n'.encode('utf-8'))

        logging.warning(f"Too many login attempts from {addr} on port {sock.getsockname()[1]}")
        conn.sendall('Too many login attempts. Connection closed.\n'.encode('utf-8'))
        conn.close()

# Create sockets and listen on the specified ports
sockets = []
for port in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen()
    #logging.info(f"Port listen {port}...")
    x = threading.Thread(target=accept_connection, args=(s,))
    x.daemon = False
    x.start()
    sockets.append(x)


for sock in sockets:
    sock.join()