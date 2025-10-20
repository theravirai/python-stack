import json

from datetime import datetime

def export_report(report_data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"reports/log_report_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(report_data, file, indent=4)

    print(f"\nReport exported to: {filename}")

def analyze_logs(filename):
    info_count = 0
    warning_count = 0
    error_count = 0

    with open(filename, "r") as file:
        logs = file.readlines()

    for log in logs:
        if "INFO" in log:
            info_count += 1

        elif "WARNING" in log:
            warning_count += 1

        elif "ERROR" in log:
            error_count += 1

    report_data = {
        "info_messages": info_count,
        "warning_messages": warning_count,
        "error_messages": error_count,
        "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\n===== LOG ANALYZER =====\n")

    print(f"INFO Messages     : {info_count}")
    print(f"WARNING Messages  : {warning_count}")
    print(f"ERROR Messages    : {error_count}")

    print("\n========================\n")

    export_report(report_data)

analyze_logs("sample.log")