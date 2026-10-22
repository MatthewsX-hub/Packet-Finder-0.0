Packet Finder 0.0

Packet Finder is a Python-based network diagnostic tool that uses the Windows ping command to test connectivity to an IP address or hostname. It collects packet statistics, calculates latency measurements, and records test results in a timestamped log file.

Features

Connectivity Testing: Sends a user-specified number of ping requests to an IP address or hostname.

Packet Loss Detection: Reports the number of packets sent, received, and lost, along with the packet-loss percentage.

Latency Measurements: Calculates minimum, average, and maximum latency from successful ping replies.

Persistent Logging: Saves test results to Packet Finder.txt, appending new entries to preserve previous results.

Error Logging: Records failures when Windows cannot resolve a hostname or the program cannot read the expected ping statistics.

Execution Timing: Measures ping execution time and result-processing time.

Input Validation: Requires a positive whole number for the requested ping count and a non-empty target.

Requirements

Windows operating system

Python 3

Standard Python libraries used by the program: subprocess, socket, os, sys, datetime, re, and time

No third-party Python packages are currently required.

How to Run

Install Python 3 if it is not already installed.

Download or clone this repository.

Open a terminal in the project directory.

Run the program:

python "Packet Finder 0.0.py"

Enter the number of ping requests.

Enter an IP address or hostname, such as 8.8.4.4 or google.com.

Review the displayed results and the generated Packet Finder.txt log file.

Example Output

How many times would you like to ping the server target? 5
Enter the server target (IP or hostname): google.com

No packet loss detected.
Packets sent: 5
Packets received: 5
Packets lost: 0
Packet loss: 0.00%
Minimum latency: 44 ms
Average latency: 54.80 ms
Maximum latency: 64 ms

Ping execution time: 4.11 seconds
Result processing time: 0.0007 seconds

Example values are illustrative and will vary depending on network conditions.

Log File

Packet Finder creates Packet Finder.txt alongside the Python script and appends timestamped entries for completed tests and handled errors.

Successful test entries include the target, packet counts, packet-loss percentage, and latency measurements. Failed hostname-resolution attempts are recorded with an error status and the corresponding Windows error message.

Current Limitations

Designed for Windows ping output; output parsing may need adjustments for other operating systems or localized Windows installations.

Latency statistics are calculated only from successful ping replies.

Jitter calculations, graphical reporting, and CSV exports are not currently implemented.

Zero packet loss during a test does not guarantee that a network connection will always be stable.

Planned Improvements

Add jitter calculations.

Improve error classification and handling.

Add CSV export for historical test results.

Improve reporting and network-performance analysis.

Project Status

Version: 0.0 — Initial Development

Packet Finder is a personal programming project focused on Python, network troubleshooting, command execution, data parsing, and diagnostic logging.

Disclaimer

This tool is intended for legitimate network troubleshooting and educational purposes. Only test systems and networks you are authorized to access.
