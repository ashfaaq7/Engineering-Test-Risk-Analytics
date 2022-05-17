'''
This program will run unit tests for the module code.py
'''

import unittest
import code
import os
import ipaddress

class TestCode(unittest.TestCase):
    
    def test_del_output_file(self):
        '''
        Function to test the deletion of Combined.csv file if alredy present.
        '''
        output_file = "Engineering Test Files\\Combined.csv"
        errors_list = ["Combined.csv file not found!", "Combined.csv file deleted successfully."]
        self.assertIn(code.del_output_file(output_file), errors_list, "Failed test_del_output_file1!")
    
    def test_read_data(self):
        '''
        Function to test the data extraction from the input csv files.
        '''
        files_list = os.listdir(input_path)
        errors_list = ["Data extraction successful."]
        self.assertIn(code.read_data(files_list, input_path, combined_data), errors_list, "Failed test_read_data!")

    def test_write_output_file(self):
        '''
        Function to test the writing of Combined.csv output csv file.
        '''
        self.test_read_data()
        errors_list = ["Combined.csv file generated successfully!"]
        sorted_dict_list = sorted(combined_data.keys(), key = ipaddress.IPv4Address)
        global out_data
        for k in sorted_dict_list:
            out_data.append({'Source IP': k, 'Environment': combined_data[k]})
        
        self.assertIn(code.write_output_file(output_file, out_data, header_row), errors_list, "Failed test_read_data!")

if __name__ == '__main__':

    input_path = "Engineering Test Files\\"
    # Output file name
    output_file = "Engineering Test Files\\Combined.csv"
    combined_data = {}
    out_data = []
    header_row = ["Source IP", "Environment"]
    unittest.main()
