import socket
import sys
import time

def send_loop(host_ip_addr, multicast_group_ip, multicast_port):
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM,\
            proto=socket.IPPROTO_UDP, fileno=None)

    multicast_group = (multicast_group_ip, multicast_port)

    sender.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

    sender.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF,\
            socket.inet_aton(host_ip_addr))

    while True:
        print("Sending data!")
        sender.sendto("test".encode(), multicast_group)
        time.sleep(1)

    sender.close()

def help_and_exit(prog):
    print('Usage: ' + prog + ' host_ip mcast_group_ip mcast_port', file=sys.stderr)
    sys.exit(1)

def main(argv):
    if len(argv) < 4: 
        help_and_exit(argv[0])

    host_ip_addr = argv[1]
    multicast_group_ip = argv[2]
    multicast_port = int(argv[3])

    send_loop(host_ip_addr, multicast_group_ip, multicast_port)

if __name__ == "__main__":
    main(sys.argv)
