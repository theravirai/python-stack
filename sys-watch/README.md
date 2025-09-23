# SYS WATCH

SYS WATCH is a lightweight Python-based system monitoring utility that displays real-time system information directly in the terminal.

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- System boot time tracking
- Active process monitoring
- JSON report export

## Technologies Used

- Python
- psutil
- JSON
- shutil
- datetime

## Project Structure

```bash
sys-watch/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

## Setup

Clone the repository:

```bash
git clone <repository-url>
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python3 main.py
```

## Example Output

```bash
========== SYS WATCH ==========

CPU Usage      : 12.4%
Memory Usage   : 58.1%
Disk Usage     : 54.32%
System Booted  : 2025-09-11 10:30:00

Top Processes:

PID: 123 | Name: Google Chrome | CPU: 12.5%
PID: 456 | Name: Code | CPU: 8.3%

===============================
```

## Future Improvements

- Live monitoring mode
- Colored terminal output
- CLI arguments
- Performance logging
- Docker support