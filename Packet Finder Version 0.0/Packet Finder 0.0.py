import subprocess
import socket
import os
import sys
from datetime import datetime
import re 
import time


LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Packet Finder.txt")
print("Log file location:", LOG_FILE)

def log_event(event): # Record a timestamped event in Packet Finder's log file 
    """Append a timestamped message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {event}\n")

try:
    packet_count = int(input("How many times would you like to ping the server target? "))

    if packet_count <= 0:
        raise ValueError

except ValueError:
    print("Error: Enter a positive whole number.")
    raise SystemExit(1)

# Executes a Windows command and returns its output
# A timeout prevents commands from running indefinitely
def run_cmd(cmd, timeout=60):
    """Run a command with a timeout and return the output."""
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            shell=False
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Error: Command timed out."
    except Exception as e:
        return f"Error: {str(e)}"

server_target = input("Enter the server target (IP or hostname): ").strip()

if not server_target:
    print("Error: Enter an IP address or hostname,")
    raise SystemExit(1)

ping_command = ["ping", "-n", str(packet_count), "-w", "1000", server_target] # Allows the user to ping the server target for a desired amount of times 
start_time = time.perf_counter()
result = run_cmd(ping_command)
ping_duration = time.perf_counter() - start_time
processing_start = time.perf_counter()
latency_text = re.findall(r"time[=<]\s*(\d+)\s*ms", result, re.IGNORECASE)
latencies = [int(value) for value in latency_text]
#print(result) # Displays the result of the ping command to the user 
loss_line = [line for line in result.splitlines() if "Lost =" in line] # Extracts the packet loss information from the ping command output
if not loss_line:
    print("Could not read packet statistics.")
    print(result)

    log_event(
        f"Target: {server_target} | "
        f"Status: Failed | "
        f"Error: {result}"
    )

    raise SystemExit(1)
loss_percent = int(loss_line[0].split("(")[1].split("%")[0])
#print(loss_percent)

# Detects whether packet loss has occurred 
if loss_percent > 0: 
    print(f"Packet loss detected: {loss_percent}%")
else:
    print("No packet loss detected.")

sent_packets = int(loss_line[0].split(" Sent = ")[1].split(",")[0])
print(f"Packets sent: {sent_packets}")

received_packets = int(loss_line[0].split(" Received = ")[1].split(",")[0])
print(f"Packets received: {received_packets}") 

lost_packets = int(loss_line[0].split("Lost = ")[1].split(" ")[0])
calculated_loss = (lost_packets / sent_packets) * 100 
print(f"Packets lost: {lost_packets}")
print(f"Packet loss: {calculated_loss:.2f}%")
if latencies:
    print(f"Minimum latency: {min(latencies)} ms")
    print(f"Average latency: {sum(latencies) / len(latencies):.2f} ms")
    print(f"Maximum latency: {max(latencies)} ms")
else:
    print("No successful ping replies to measure latency.")

min_latency = min(latencies) if latencies else "N/A"
average_latency = (
    f"{sum(latencies) / len(latencies):.2f}"
    if latencies else "N/A"
)
max_latency = max(latencies) if latencies else "N/A"

log_event(
    f"Target: {server_target} | "
    f"Sent: {sent_packets} | "
    f"Received: {received_packets} | "
    f"Lost: {lost_packets} | "
    f"Packet loss: {calculated_loss:.2f}% | "
    f"Min latency: {min_latency} ms | "
    f"Average latency: {average_latency} ms | "
    f"Max latency: {max_latency} ms"
)

processing_duration = time.perf_counter() - processing_start 

print(f"Results saved to {LOG_FILE}")
print(f"Ping execution time: {ping_duration:.2f} seconds")
print(f"Result processing time: {processing_duration:.4f} seconds")