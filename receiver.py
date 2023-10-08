import socket
import struct
import sys

BUFSIZE = 1024

def help_and_exit(prog):
    print('Usage: ' + prog + ' from_nic_by_host_ip multicast_group_ip, multicast_port')
    sys.exit(1)

def receive_loop(from_nic_ip, multicast_group_ip, multicast_port):
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM,\
            proto=socket.IPPROTO_UDP, fileno=None)
    multicast_group = (multicast_group_ip, multicast_port)
    receiver.bind(multicast_group)

    if from_nic_ip == '0.0.0.0':
        mreq = struct.pack("=4sl", socket.inet_aton(multicast_group_ip), socket.INADDR_ANY)
    else:
        mreq = struct.pack("=4s4s",\
                socket.inet_aton(multicast_group_ip), socket.inet_aton(from_nic_ip))
    receiver.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        buf, _ = receiver.recvfrom(BUFSIZE)
        msg = buf.decode()
        print(msg)

    reciver.close()

def main(argv):
    if (len(argv) < 4):
        help_and_exit(argv[0])

    from_nic_ip = argv[1]
    multicast_group_ip = argv[2]
    multicast_port = int(argv[3])

    receive_loop(from_nic_ip, multicast_group_ip, multicast_port)

if __name__ == '__main__':
    main(sys.argv)
