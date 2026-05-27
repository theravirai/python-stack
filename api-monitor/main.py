import requests
import time
import json
import argparse

from datetime import datetime

def save_log(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"logs/api_log_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"\nLog saved to: {filename}")

def check_api(url):
    try:
        start_time = time.time()

        response = requests.get(url)

        end_time = time.time()

        response_time = round(end_time - start_time, 3)

        api_data = {
            "url": url,
            "status_code": response.status_code,
            "response_time": response_time,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        print("\n===== API MONITOR =====\n")

        print(f"URL            : {url}")
        print(f"Status Code    : {response.status_code}")
        print(f"Response Time  : {response_time} seconds")

        print("\n=======================\n")

        save_log(api_data)

    except requests.exceptions.RequestException as error:
        print("\n===== API ERROR =====\n")

        print(f"Failed to connect to: {url}")
        print(f"Error: {error}")

        print("\n=====================\n")

parser = argparse.ArgumentParser()

parser.add_argument(
    "--url",
    required=True,
    help="API URL to monitor"
)

args = parser.parse_args()

check_api(args.url)