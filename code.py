'''
This program will read Server IPs from each environment csv files under the "Engineering Test Files" folder
and combine all the Server IPs and Environment names in a single 'Combined.csv' file
'''

import os
import csv
import re
import ipaddress

def del_output_file(output_file):
    '''
    Delete the Combined.csv output file
    '''
    try:
        os.remove(output_file)
    except FileNotFoundError:
        return "Combined.csv file not found!"
    # except PermissionError:
    #     return "Permission denied!"
    
    return "Combined.csv file deleted successfully."

def read_data(files_list, input_path, all_data):
    '''
    Loop through each csv file in the input_path folder
    '''
    for i in files_list:
        # Full file path
        file_path = input_path + i

        # Generate the Environment name by removing the numbers and file extension (.csv) from the file name
        environment_name = re.sub(" \d+", "", os.path.splitext(i)[0])
        
        try:
            # Read each csv file
            print(f"Reading file: {file_path}")
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                # Skip the header line of the csv file
                next(f)
                data = csv.reader(f)
                # Loop through the data and add the Source IP & environment to the dictionary
                for j in list(data):
                    # Fetch the first item in the data to get the Source IP
                    # Add it to the dictionary if it is not already present
                    if j[0] not in all_data.keys():
                        all_data[j[0]] = environment_name
                    else:
                        continue
        except:
            return "Error while reading the csv file!"
        global combined_data
        combined_data = all_data
    return "Data extraction successful."

def write_output_file(output_file, out_data, header_row): 
    '''
    Write Combined.csv output file
    '''
    try:
        with open(output_file, 'w', newline='') as outputfile: 
            # Create a csv dict writer obj
            writer = csv.DictWriter(outputfile, fieldnames = header_row) 
            # Write header in the first row of the file
            writer.writeheader() 
            # Write the data
            writer.writerows(out_data) 
    except:
        return "Error while writing the Combined.csv file!"

    return "Combined.csv file generated successfully!"

if __name__ == "__main__":
    # Assuming this python program is in the same path as the 'Engineering Test Files' folder
    input_path = "Engineering Test Files\\"
    # Output file name
    output_file = "Engineering Test Files\\Combined.csv"

    # Remove the Combined.csv file if it already exists
    del_output_file(output_file)

    # Get all the files present under the input_path folder
    files_list = os.listdir(input_path)

    # Dict to store the data for Combined.csv
    combined_data = {}

    # Read the data from input files
    read_data(files_list, input_path, combined_data)

    # Sort based on ascending order of the Source IPs
    sorted_dict_list = sorted(combined_data.keys(), key = ipaddress.IPv4Address)
    out_data = []

    for k in sorted_dict_list:
        out_data.append({'Source IP': k, 'Environment': combined_data[k]})

    # print(out_data)

    # Header of the Combined.csv file
    header_row = ['Source IP', 'Environment'] 

    write_output_file(output_file, out_data, header_row)
