import re

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


def main():
    logs = parse_log_file(LOG_FILE)

    print("Parsed log entries:")
    for log in logs:
        print(log)


if __name__ == "__main__":
    main()