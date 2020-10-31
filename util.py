# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:13:49 2020

@author: mehedi.md.hasan
import, var_files,pip_install_upper_constraints_proto 

"""
import os, yaml, re, configparser, ast, tokenize, csv, time, pandas
from os import path

class Util:
    
    def __init__(self):

        self.__files = {}
        self.__python_files =[]
        self.__yaml_files = []
        self.__tox_files = []
        
        
    def __write_to_arr(self, file_path):

        name, extension = os.path.splitext(file_path)
       
        if extension == ".py":
            self.__python_files.append(file_path)
#            print(f'Python file: {file_path}')
        
        if extension in [".yml", ".yaml"]:
            self.__yaml_files.append(file_path)
#            print(f'YML file: {file_path}')

        if extension == ".ini":
            self.__tox_files.append(file_path)
#            print(f'Tox file: {file_path}')
        
        
        
   
    
    def __traverse(self, base_dir):
        
        for (dirpath, dirnames, filenames) in os.walk(base_dir):
            for filename in filenames:
                if filename == "tox.ini":           
                    self.__write_to_arr(os.path.normpath(os.path.join(base_dir, dirpath, filename)))
            
            for dirname in dirnames:
                if dirname == "tests":
                    test_path = os.path.join(dirpath, dirname)
                    
                    for (testdirpath, testdirnames, testfilenames) in os.walk(test_path):
                        for testfile in testfilenames:
                            self.__write_to_arr(os.path.normpath(os.path.join(test_path,testdirpath, testfile)))




    def get_files(self, base_dir):
        
        self.__traverse(base_dir)

        self.__files["python"] = self.__python_files
        self.__files["yaml"] = self.__yaml_files
        self.__files["tox"] = self.__tox_files
        
#        print (f'Pyhon files: {self.__files["python"]}')
#        print (f'\n ==\n Yaml files: {self.__files["yaml"]}')
#        print (f'\n == \n Tox files: {self.__files["tox"]}')
        
#        print(self.__files)
        return self.__files
    
    def get_playbook( yaml_file_path):
        with open(yaml_file_path, 'r') as f:
            playbook = yaml.load(f)
        
        return playbook
    
    def get_tox_configs(tox_file_path):
        configs = configparser.ConfigParser()
        configs.read(tox_file_path)
        return configs
    
    def get_python_tokenized_file(filename):
        with tokenize.open(filename) as f:
            return ast.parse(f.read(), filename=filename)
    
        
    
    def write_to_file(self,anti_pattern_name, test_file_name, anti_pattern_count):
#        print(f"Entered Here: {anti_pattern_name}")
        headers = ['file_name','Skip_Ansible_Lint', 'Local_Only_Test', 'Assertion_Roulette', 'External_Dependency', 'No_ENV_CleanUp' ]
        if path.exists("output.csv") and (time.time() - os.path.getctime("output.csv"))<3600:
            print (f'appending in current output file.\nTest File Name: {test_file_name}\nDetected Antipattern: {anti_pattern_name}')
            self.append_antipattern(test_file_name, anti_pattern_name, anti_pattern_count)
            
                
        else:
            print("Creating a new csv file")
            try:
                self.__create_new_output_file(headers, 'output.csv')
                self.append_antipattern(test_file_name, anti_pattern_name, anti_pattern_count)
                
                
            except:
                print("Could not create output file")

#    def __is_same_file(self, outfile, filepath):
#        last_line = self.__find_last_line(outfile)
        
        
    
    def __create_new_output_file(self, headers, filename):
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames = headers)
            csv_writer.writeheader()
            
    def append_antipattern(self, test_file_name, anti_pattern_name, anti_pattern_count):
        try:
            last_line = self.__find_last_line_panda('output.csv')
#            print(f'last_line: {last_line}')
#            print(test_file_name)
            
            if last_line['file_name'] == os.path.normpath(test_file_name):
                try:
                    anti_pattern_current_count = int (last_line[anti_pattern_name])
                    anti_pattern_new_count = anti_pattern_current_count + anti_pattern_count
                    self.update_csv_line_panda(r'output.csv', test_file_name, anti_pattern_name, anti_pattern_new_count)    
                except:
                    print("Antipattern not found")
        except:
            print("output file does not have any row")
            self.update_csv_line_panda(r'output.csv', test_file_name, anti_pattern_name, anti_pattern_count)
        
        
        
        
#        writer.writerow(data) 
#        print(f'{filepath} has {antipattern_count} no of suspected {anti_pattern_name}  antipattern of IaC Testing')
        
    
    def is_substring( substrings, long_string):
        
        return any (sstr in long_string for sstr in substrings)
        
#        for substring in substrings:
#            if substring in long_string:
#                return True
#        return False
#        
    def has_pattern_regex(pattern, long_string):
        return re.search(pattern, long_string) != None
        


#    def output_exists ():
#        
#        return path.exists("output.csv") and (time.time() - os.path.getctime("output.csv"))<3600
        
    
#    def __find_last_line(self, file_name):
#        with open (file_name) as f:
#            csv_reader = csv.DictReader(f)
#            row_count = 0
#            rows = []
#            for row in csv_reader:
#                row_count +=1
#                rows.append(row)
#            
#        csv_details = {}
#        csv_details['row_count'] = row_count - 1
#        last_row = rows[row_count -2]
#        csv_details['file_name'] = last_row['file_name']
#        csv_details['skip_linting'] = last_row['skip_linting']
#        csv_details['local_host_testing'] = last_row['local_host_testing']
#        csv_details['assertion_roulette'] = last_row['assertion_roulette']
#        csv_details['external_dependency'] = last_row['external_dependency']
#        csv_details['test_env_not_cleaned'] = last_row['test_env_not_cleaned']
#        
#        return csv_details
    
    def find_last_line_panda(self, file_name):
        df = pandas.read_csv(file_name)
        last_row = df.shape[0] - 1
        return df.loc[last_row, :]
    
    def update_csv_line_panda(self, output_file_name, test_file_name, column_name, new_value):
        df = pandas.read_csv(output_file_name, index_col='file_name')
        df.at[test_file_name, column_name] = new_value
        print(df)
        df.to_csv(output_file_name)
#        return df.loc[line_no,column_name]
        
        