def analyze_log(file_path):
    total_lines = 0
    levels = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    error_messages = {}

    try:
        with open(file_path, "r") as file:
            for line in file:
                total_lines += 1
                line = line.strip()

                if line.startswith("INFO"):
                    levels["INFO"] += 1
                
                elif line.startswith("WARNING"):
                    levels["WARNING"] += 1

                elif line.startswith("ERROR"):
                    levels["ERROR"] += 1
                    message = line.replace("ERROR", "").strip()
                    error_messages[message] = error_messages.get(message, 0) + 1
    except FileNotFoundError:
        print("Log file not found.")
        return
    
    print("\n--- Log Analysis Report ---")
    print(f"Total log entries: {total_lines}")
    print(f"INFO logs: {levels['INFO']}")
    print(f"WARNING logs: {levels['WARNING']}")
    print(f"ERROR logs: {levels['ERROR']}")

    if error_messages:
        print("\nMost Common Errors: ")
        for msg, count in error_messages.items():
            print(f"- {msg} ({count} times)")

    
def main():
    file_path = input("Enter log file name (e.g.sample.log): ").strip()
    analyze_log(file_path)


if __name__ == "__main__":
    main()