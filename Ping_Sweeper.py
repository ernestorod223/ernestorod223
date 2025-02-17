import sys
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork

def ping_sweeper(network, netmask):
    live_hosts = []
    total_hosts = 0
    scanned_hosts = 0

    ip_network = IPNetwork(network + '/' + netmask)
    for hosts in ip_network.iter_hosts():
        total_hosts += 1

    for host in ip_network.iter_hosts():
        scanned_hosts += 1
        print(f"Scanning: {scanned_hosts}/{total_hosts}", end='\r')
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is not None:
            live_hosts.append(str(host))
            print(f"Host {host} is live.")

    return live_hosts

if __name__ == "__main__":
    network = sys.argv[1]
    netmask = sys.argv[2]

    live_hosts = ping_sweeper(network, netmask)
    print(f"Live hosts: {live_hosts}")