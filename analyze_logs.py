import os
import subprocess
import re
from collections import Counter
from rich.console import Console
from rich.table import Table




LOG_FILE    = "sample.log"
console     = Console()

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

def print_log_entry_table(logs):
    table = Table(title="Parsed Log Entries")
    table.add_column("IP")
    table.add_column("Method")
    table.add_column("Path")
    table.add_column("status")

    for log in logs:
        table.add_row(
            log["ip"],
            log["method"],
            log["path"],
            str(log["status"]),
        )
    
    console.print(table)

def print_status_table(status_counts):
    table = Table(title="HTTP Status Code Summary")
    table.add_column("Status Code", justify="right")
    table.add_column("Count",       justify="right")

    for status, count in sorted(status_counts.items()):
        table.add_row(str(status),str(count))
    
    console.print(table)

def print_endpoint_table(endpoint_counts):
    table = Table(title="Top Endpoints")
    table.add_column("Endpoint")
    table.add_column("Requests",    justify="right")

    for path, count in sorted(endpoint_counts.most_common(5)):
        table.add_row(path,str(count))
    
    console.print(table)

def print_error_table(errors, title):
    table = Table(title=title)
    table.add_column("Status", justify="right")
    table.add_column("Method")
    table.add_column("Path")
    table.add_column("IP Address")

    if errors:
        for error in errors:
            table.add_row(
                str(error["status"]),
                error["method"],
                error["path"],
                error["ip"],
            )
    else:
        table.add_row("-","-","no errors detected","-")
    
    console.print(table)

def main():
    logs = parse_log_file(LOG_FILE)
    status_counts = count_status_codes(logs)
    endpoint_counts = count_endpoints(logs)
    client_errors, server_errors = detect_errors(logs)


    _ = subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
    
    print_log_entry_table(logs)

    print("\n"*2)

    print_status_table(status_counts)

    print("\n" * 2)

    print_endpoint_table(endpoint_counts)

    print("\n" * 2)

    print_error_table(client_errors, "Client Errors (4xx)")

    print("\n" * 2)

    print_error_table(server_errors, "Server Errors (5xx)")

if __name__ == "__main__":
    main()