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

def main():
    logs = parse_log_file(LOG_FILE)
    status_counts = count_status_codes(logs)

    _ = subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
    
    print("Parsed log entries:")
    print("=" * 30)
    for log in logs:
        print(log)

    print("\n"*2)

    print("HTTP Status Code Summary")
    print("=" * 30)

    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")

if __name__ == "__main__":
    main()