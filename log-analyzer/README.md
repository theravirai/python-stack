# LOG ANALYZER

LOG ANALYZER is a lightweight Python utility for analyzing server-style log files and generating structured JSON reports.

## Features

- Reads log files
- Counts INFO messages
- Counts WARNING messages
- Counts ERROR messages
- Generates JSON analysis reports

## Technologies Used

- Python
- JSON
- datetime

## Project Structure

```bash
log-analyzer/
├── reports/
├── sample.log
├── main.py
├── requirements.txt
└── README.md
```

## Example Log File

```txt
INFO: Server started successfully
WARNING: High memory usage detected
ERROR: Failed to fetch user data
```

## Example Output

```bash
===== LOG ANALYZER =====

INFO Messages     : 4
WARNING Messages  : 2
ERROR Messages    : 2

========================
```