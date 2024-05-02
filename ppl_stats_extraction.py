import os
import re
import csv

def extract_ppl_values(log_directory):
    # Regular expression to find the ppl values
    regex = r"ppl:\s*([0-9.]+)"

    # Prepare to collect the results in a dictionary
    results = {}

    # Go through each file in the directory
    for filename in os.listdir(log_directory):
        if filename.endswith(".log"):  # Check if it's a log file
            file_path = os.path.join(log_directory, filename)
            with open(file_path, 'r') as file:
                ppl_values = []
                for line in file:
                    match = re.search(regex, line)
                    if match:
                        ppl_values.append(float(match.group(1)))
                results[filename] = ppl_values

    # Writing results to CSV
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = list(results.keys())
        headers.append("validation ppl")  # Add the new column name for validation ppl
        writer.writerow(headers)  # Write the headers including the new column

        # Initialize the step value for "validation ppl"
        validation_ppl = 500

        rows = zip(*results.values())
        for row in rows:
            writer.writerow(list(row) + [validation_ppl])  # Write each row and add the current validation ppl value
            validation_ppl += 500  # Increment the validation ppl value by 500 for the next row


# Specify the directory containing the log files
log_directory = 'training_logs'
extract_ppl_values(log_directory)
