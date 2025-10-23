# API MONITOR

API MONITOR is a lightweight Python utility for monitoring API availability, response times, and request health.

## Features

- Sends HTTP GET requests
- Measures API response time
- Displays HTTP status codes
- Handles request failures gracefully
- Generates JSON monitoring logs

## Technologies Used

- Python
- requests
- JSON
- datetime

## Example Output

```bash
===== API MONITOR =====

URL            : https://api.github.com
Status Code    : 200
Response Time  : 0.312 seconds

=======================
```

## Example JSON Log

```json
{
    "url": "https://api.github.com",
    "status_code": 200,
    "response_time": 0.312
}
```