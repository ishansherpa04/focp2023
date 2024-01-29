import sys

def read_cat_shelter_log(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read lines from the file, split each line into a list using commas as separators,
            # and strip any leading or trailing whitespaces from each element
            return [line.strip().split(',') for line in file]
    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

def analyze_cat_visits(log_data):
    # Initialize variables to store various statistics
    cat_visits = 0
    intruder_count = 0
    total_time_in_house = 0
    min_duration = float('inf')
    max_duration = 0
    total_duration = 0

    # Iterate through each entry in the log data
    for data in log_data:
        # Check if the entry corresponds to your cat ("OURS")
        if data[0] == 'OURS':
            # Increment cat_visits counter
            cat_visits += 1
            # Extract start and end times, calculate duration
            start_time, end_time = map(int, data[1:3])
            duration = end_time - start_time
            # Update various statistics
            total_duration += duration
            total_time_in_house += duration
            min_duration = min(min_duration, duration)
            max_duration = max(max_duration, duration)
        # Check if the entry corresponds to other cats ("THEIRS")
        elif data[0] == 'THEIRS':
            # Increment intruder_count counter
            intruder_count += 1

    # Return the calculated statistics
    return cat_visits, intruder_count, total_time_in_house, min_duration, max_duration, total_duration

def print_analysis(cat_visits, intruder_count, total_time_in_house, min_duration, max_duration, total_duration):
    # Print the analysis results based on the calculated statistics
    if cat_visits == 0:
        print("No cat visits found.")
    else:
        print("Log File Analysis")
        print("==================\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {intruder_count}")
        print(f"Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n")
        print(f"Average Visit Length: {total_duration // cat_visits} Minutes")
        print(f"Longest Visit: {max_duration} Minutes")
        print(f"Shortest Visit: {min_duration} Minutes")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # Extract file_path from command-line arguments
    file_path = sys.argv[1]
    # Read log data from the specified file
    log_data = read_cat_shelter_log(file_path)
    
    # Check if log_data is not empty
    if log_data:
        # Analyze cat visits and get statistics
        cat_visits, intruder_count, total_time_in_house, min_duration, max_duration, total_duration = analyze_cat_visits(log_data)
        # Print the analysis results
        print_analysis(cat_visits, intruder_count, total_time_in_house, min_duration, max_duration, total_duration)
