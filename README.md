# My_Portsccaner
🔍 Python Port Scanner 

protsccaner(1) for windows and portsccaner(2) for kali linux 
A lightweight TCP port scanner written in Python designed to run smoothly on Windows 11.
This tool allows users to scan a custom port range on a target IP address and identify open ports using socket-based connections.

📌 Features

✅ Manual IP address input

✅ Custom start & end port selection

✅ Fast TCP scanning using socket.connect_ex()

✅ Displays open and closed ports in real-time

✅ Stores all open ports in a list

✅ Windows-friendly (no Linux-only dependencies)

🛠️ Technologies Used

Language: Python 3

Library: socket (built-in)

Platform Tested: Windows 11 for portsccaner(1) and kali linux for portsccaner(2)

🚀 How It Works

The user enters:

Target IP address

Starting port

Ending port

The scanner attempts a TCP connection to each port in the given range.

If the connection succeeds, the port is marked as OPEN.

All open ports are stored and displayed at the end of the scan.

▶️ Usage
1️⃣ Clone the repository
git clone https://github.com/dhuruvkoli41/python-port-scanner.git
cd python-port-scanner

2️⃣ Run the script
python port_scanner.py

3️⃣ Sample Input
Enter the IP address: 127.0.0.1
Enter the port to start the scan from: 1
Enter the port to stop the scan on: 1000

4️⃣ Sample Output
the port number 80 is open
the port number 443 is open
----------------------------------------
the scanning is done ....
the ports which are open are :
[80, 443]

⚠️ Important Notes

🔐 Run scans only on systems you own or have permission to test

🧱 Firewalls or antivirus software may block or interfere with scans

⏱️ Lower timeouts increase speed but may miss filtered ports

📈 Future Improvements

 Multithreaded scanning for faster performance

 Service/banner detection

 Export results to file (TXT / JSON)

 Exception handling & input validation

 Stealth scanning techniques

🎯 Learning Outcomes

Understanding TCP socket communication

Practical experience with network scanning

Basics of reconnaissance in cybersecurity

Writing platform-compatible Python tools

👨‍💻 Author

Dhuruv Koli
B.Tech CSE | Cybersecurity Enthusiast
🔗 GitHub: https://github.com/dhuruvkoli41/

📜 Disclaimer

This project is for educational purposes only.
The author is not responsible for misuse of this tool.
