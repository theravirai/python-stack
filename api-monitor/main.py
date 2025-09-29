import requests
import time

def check_api(url):
    start_time = time.time()

    response = requests.get(url)

    end_time = time.time()

    response_time = round(end_time - start_time, 3)

    print("\n===== API MONITOR =====\n")

    print(f"URL            : {url}")
    print(f"Status Code    : {response.status_code}")
    print(f"Response Time  : {response_time} seconds")

    print("\n=======================\n")

check_api("https://api.github.com")