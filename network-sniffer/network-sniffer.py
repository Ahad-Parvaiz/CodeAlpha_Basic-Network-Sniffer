from scapy.all import *
import sys
from datetime import datetime

def packet_callback(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    src_ip = dst_ip = protocol = payload = src_port = dst_port = "N/A"
    
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        proto_names = {1: "ICMP", 6: "TCP", 17: "UDP"}
        protocol = proto_names.get(protocol, str(protocol))
        
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        
        if packet.haslayer(Raw):
            payload = packet[Raw].load.hex()[:32] + "..." if len(packet[Raw].load.hex()) > 32 else packet[Raw].load.hex()
    
    print(f"[{timestamp}]")
    print(f"Source IP: {src_ip}")
    print(f"Destination IP: {dst_ip}")
    print(f"Protocol: {protocol}")
    print(f"Source Port: {src_port}")
    print(f"Destination Port: {dst_port}")
    print(f"Payload (hex): {payload}")
    print("-" * 50)

def main():
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run with sudo.")
        sys.exit(1)
    
    try:
        print("Starting network sniffer... Press Ctrl+C to stop")
        sniff(prn=packet_callback, store=0, filter="tcp")  # Filter for TCP, no count limit
    except KeyboardInterrupt:
        print("\nSniffer stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
