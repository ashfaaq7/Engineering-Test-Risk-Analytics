'''
This program will read Server IPs from each environment csv files under the "Engineering Test Files" folder
and combine all the Server IP and Environment in a single 'Combined.csv' file
'''

import os
import csv
import re
import ipaddress

if __name__ == "__main__":
    # Assuming this python program is in the same path as the 'Engineering Test Files' folder
    input_path = "Engineering Test Files\\"

    # Remove the Combined.csv file if it already exists
    try:
        os.remove(input_path + "Combined.csv")
    except FileNotFoundError:
        print("Combined.csv file not found!")
    else:
        print("Combined.csv file deleted successfully.")

    # Get all the files present under the input_path folder
    files_list = os.listdir(input_path)

    # Dict to store the data for Combined.csv
    combined_data = {}

    # Loop through each csv file in the input_path folder
    for i in files_list:
        # Full file path
        file_path = input_path + i

        # Generate the Environment name by removing the numbers and file extension (.csv) from the file name
        environment_name = re.sub(" \d+", "", os.path.splitext(i)[0])
        
        try:
            # Read each csv file
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                # Skip the header line of the csv file
                next(f)
                data = csv.reader(f)
            
                # Loop through the data and add the Source IP & environment to the dictionary
                for j in list(data):
                # Fetch the first item in the data to get the Source IP
                # Add it to the dictionary if it is not already present
                    if j[0] not in combined_data.keys():
                        combined_data[j[0]] = environment_name
                    else:
                        continue
        except:
            print(f"Error while reading the csv file: {file_path}!")
        else:
            print(f"Data extraction successful from file: {file_path}")
            
    # Sort based on ascending order of the Source IPs
    sorted_dict_list = sorted(combined_data.keys(), key = ipaddress.IPv4Address)
    out_data = []

    for k in sorted_dict_list:
        out_data.append({'Source IP': k, 'Environment': combined_data[k]})

    # print(out_data)

    # Header of the Combined.csv file
    header_row = ['Source IP', 'Environment'] 

    # Output file name
    output_file = "Engineering Test Files\\Combined.csv"
        
    # Write Combined.csv output file 
    try:
        with open(output_file, 'w', newline='') as outputfile: 
            # Create a csv dict writer obj
            writer = csv.DictWriter(outputfile, fieldnames = header_row) 
            # Write header in the first row of the file
            writer.writeheader() 
            # Write the data
            writer.writerows(out_data) 
    except:
        print("Error while writing the Combined.csv file!")
    else:
        print("Combined.csv file generated successfully!")
