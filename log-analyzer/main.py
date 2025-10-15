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

    print("\n===== LOG ANALYZER =====\n")

    print(f"INFO Messages     : {info_count}")
    print(f"WARNING Messages  : {warning_count}")
    print(f"ERROR Messages    : {error_count}")

    print("\n========================\n")

analyze_logs("sample.log")