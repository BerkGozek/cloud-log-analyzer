# Cloud Log Analyzer

A Python CLI tool that parses web server logs and generates traffic and error reports.

## Features

- Parses server log files
- Extracts IP address, HTTP method, endpoint, and status code
- Summarizes HTTP status codes
- Identifies most frequently requested endpoints
- Detects client errors (4xx) and server errors (5xx)
- Displays results in formatted CLI tables using Rich

## Technologies Used

- Python
- Rich
- Regular Expressions (`re`)
- Collections (`Counter`)

## Project Structure

```text
cloud-log-analyzer/
├── analyze_logs.py
├── sample.log
├── requirements.txt
├── README.md
└── .gitignore