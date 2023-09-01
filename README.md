# Simple-Port-Scanner-using-python
This Python script is a straightforward port scanner designed to efficiently check the status of specific ports on a target host. It offers improved functionality, error handling, and flexibility for port scanning tasks.

# Usage
To use the script, follow this command-line format:

python3 scanner.py <target_host> <start_port> <end_port>


<target_host>: Specify the target hostname or IP address.
<start_port>: Define the starting port of the scan range.
<end_port>: Define the ending port of the scan range.


# Features
Custom Port Range: You can specify a custom range of ports to scan, allowing for fine-grained control over the scanning process.

Error Handling: The script provides robust error handling, including handling hostname resolution issues and connection problems. It gracefully exits in case of unexpected interruptions.

Detailed Output: The script provides detailed output, indicating which ports within the specified range are open on the target host.

Timestamping: It logs the time when the scan started, making it easy to track when the scan was performed.

This port scanner is a versatile tool for network administrators, security professionals, and enthusiasts who need precise information about the status of network ports on a given target. Please use it responsibly and only on systems and networks for which you have proper authorization.
