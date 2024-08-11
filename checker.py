import json

def check_x17(log_file_path):
    # Read the log.json file
    with open(log_file_path, 'r') as log_file:
        data = json.load(log_file)

    # Get the value of x17 from the registers
    x17_value = data['registers'].get('x17', None)

    # Check if x17 is 0
    if x17_value == "0":
        print("Test case passed")
    else:
        print("Test case failed")

def main():
    log_file_path = "log.json"  # Path to the log.json file
    check_x17(log_file_path)

if __name__ == "__main__":
    main()
