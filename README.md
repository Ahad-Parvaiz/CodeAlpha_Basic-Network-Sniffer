# 🕵️‍♂️ Python Network Sniffer

A simple Python-based network sniffer that captures and logs details about TCP packets on your network in real time using `scapy`. It includes timestamps, source and destination IPs, ports, protocol types, and raw payloads in hexadecimal.

---

## 🔧 Features

- Captures live TCP traffic using `scapy`
- Displays:
  - Timestamp of packet capture
  - Source & Destination IP addresses
  - Protocol type (TCP, UDP, ICMP)
  - Source & Destination ports (if applicable)
  - First 32 bytes of raw payload (in hexadecimal)
- Clean and readable terminal output
- Requires **root privileges** to run

---

## 📁 File Structure

├── network-sniffer.py # Main sniffer script
└── README.md # This documentation file

---

## 🛠️ Requirements

- Python 3
- `scapy` library
- Kali Linux or any Linux system with root access

Install required packages:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install scapy
```

If you're on Kali Linux and get the externally-managed-environment error:
```sudo apt install python3-scapy```

▶️ Usage
1. Make the script executable:
  ```chmod +x network-sniffer.py```
2. Run with root privileges:
  ```sudo python3 network-sniffer.py```
3. Output example:
  ```[2025-07-28 14:24:34]
Source IP: 192.168.161.128
Destination IP: 34.36.***.***
Protocol: TCP
Source Port: 32992
Destination Port: 443
Payload (hex): 16030**************************...
--------------------------------------------------
```
## 🔗 Connect With Me

- 👨‍💼 [LinkedIn Profile](https://www.linkedin.com/in/ahadparvaiz/)
- 📢 [LinkedIn Post](https://www.linkedin.com/posts/ahadparvaiz_cybersecurity-codealpha-python-activity-7355913085192151041-cZCd?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAFg8YEcB1j52uuVGVcbs0wbLbtwAFNKvJrI)


Press Ctrl + C to stop sniffing.

⚠️ Disclaimer
This tool is for educational and ethical purposes only. Do not use it on networks you do not own or have explicit permission to monitor. Unauthorized packet sniffing may violate laws and privacy policies.
