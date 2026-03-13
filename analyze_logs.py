import os
import subprocess
import re
from collections import Counter




LOG_FILE = "sample.log"

# Regex pattern to extract fields
log_pattern = re.compile(
    r'(?P<ip>\S+) .* "(?P<method>\S+) (?P<path>\S+) .*" (?P<status>\d+)'
)

def parse_log_file(file_path):
    parsed_logs = []

    with open(file_path, "r") as f:
        for line in f:
            match = log_pattern.search(line)

            if match:
                log_entry = {
                    "ip": match.group("ip"),
                    "method": match.group("method"),
                    "path": match.group("path"),
                    "status": int(match.group("status")),
                }

                parsed_logs.append(log_entry)

    return parsed_logs

def count_status_codes(logs):
    status_counter = Counter()

    for log in logs:
        status_counter[log["status"]] +=1
    
    return status_counter

def count_endpoints(logs):
    endpoint_counter = Counter()

    for log in logs:
        endpoint_counter[log["path"]] +=1
    
    return endpoint_counter

def detect_errors(logs):
    client_errors = []
    server_errors = []

    for log in logs:
        status  = log["status"]

        if 400 <= status < 500:
            client_errors.append(log)
        elif 500 <= status <600:
            server_errors.append(log)
    
    return client_errors,server_errors

def main():
    logs = parse_log_file(LOG_FILE)
    status_counts = count_status_codes(logs)
    endpoint_counts = count_endpoints(logs)
    client_errors, server_errors = detect_errors(logs)


    _ = subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
    
    print("Parsed log entries:")
    print("=" * 30)
    for log in logs:
        print(log)

    print("\n"*2)

    print("HTTP Status Code Summary")
    print("=" * 30)

    for status, count in sorted(status_counts.items()):
        print(f"{status}:\t{count}")

    print("\n" * 2)

    print("Top Endpoints")
    print("=" * 30)

    for path,count in endpoint_counts.most_common(5):
        print(f"{path}:\t{count} requests")

    print("\n" * 2)

    print("Client errors (4xx)")

    print("=" * 30)

    if client_errors:
        for error in client_errors:
            print(f"{error["status"]} {error["method"]} {error["path"]} from {error["ip"]}")
    else:
        print("No Client Errors Detected")

    print("\n" * 2)

    print("Server errors (5xx)")

    print("=" * 30)

    if server_errors:
        for error in server_errors:
            print(f"{error["status"]} {error["method"]} {error["path"]} from {error["ip"]}")
    else:
        print("No Server Errors Detected")

if __name__ == "__main__":
    main()