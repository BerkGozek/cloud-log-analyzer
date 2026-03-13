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
```

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/cloud-log-analyzer.git
cd cloud-log-analyzer
```

### 2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash 
pip install -r requirements.txt
```

## Run the Project

```bash
python analyze_logs.py
```

## Example Output

The program generates:

- a parsed log table
- HTTP status code summary
- top endpoints
- client error report
- server error report

Example:

```text
Cloud Log Analysis Report

               Parsed Log Entries               
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┓
┃ IP Address   ┃ Method ┃ Path        ┃ Status ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━┩
│ 192.168.1.10 │ GET    │ /index.html │    200 │
│ 192.168.1.11 │ GET    │ /login      │    401 │
│ 192.168.1.10 │ POST   │ /login      │    200 │
│ 192.168.1.12 │ GET    │ /dashboard  │    500 │
│ 192.168.1.10 │ GET    │ /profile    │    200 │
│ 192.168.1.13 │ GET    │ /unknown    │    404 │
└──────────────┴────────┴─────────────┴────────┘

   HTTP Status Code    
        Summary        
┏━━━━━━━━━━━━━┳━━━━━━━┓
┃ Status Code ┃ Count ┃
┡━━━━━━━━━━━━━╇━━━━━━━┩
│         200 │     3 │
│         401 │     1 │
│         404 │     1 │
│         500 │     1 │
└─────────────┴───────┘

      Top Endpoints       
┏━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Endpoint    ┃ Requests ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ /login      │        2 │
│ /index.html │        1 │
│ /dashboard  │        1 │
│ /profile    │        1 │
│ /unknown    │        1 │
└─────────────┴──────────┘

             Client Errors (4xx)             
┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Status ┃ Method ┃ Path     ┃ IP Address   ┃
┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│    401 │ GET    │ /login   │ 192.168.1.11 │
│    404 │ GET    │ /unknown │ 192.168.1.13 │
└────────┴────────┴──────────┴──────────────┘

              Server Errors (5xx)              
┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Status ┃ Method ┃ Path       ┃ IP Address   ┃
┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│    500 │ GET    │ /dashboard │ 192.168.1.12 │
└────────┴────────┴────────────┴──────────────┘
```

## Use Case

This project simulates a lightweight cloud / DevOps monitoring utility for analyzing server traffic and identifying errors in log files.

## Future Improvements

- Support multiple log files
- Export reports to CSV
- Detect suspicious IP activity
- Add command-line arguments for custom input files

## Author

**Berk Gozek**
<br>Boston University — B.S. Data Science, Minor Computer Science
<br> GitHub: https://github.com/BerkGozek 
