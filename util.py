# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:13:49 2020

@author: mehedi.md.hasan
import, var_files,pip_install_upper_constraints_proto 

"""
import os, re, configparser, ast, tokenize, csv, time, pandas, yaml
from os import path

class Util:
    
    def __init__(self):

        self.__files = {}
#        self.__python_files =[]
        self.__yaml_files = []
#        self.__tox_files = []
        
        
    def __write_to_arr(self, file_path):

        name, extension = os.path.splitext(file_path)
#        print(f'name: {name}, extension: {extension}')
       
#        if extension == ".py":
#            self.__python_files.append(file_path)
#            print(f'Python file: {file_path}')
        
        if extension in [".yml", ".yaml"]:
            self.__yaml_files.append(file_path)
#            print(f'YML file: {file_path}')

#        if extension == ".ini":
#            print(file_path)
#            self.__tox_files.append(file_path)
#            print(f'Tox file: {file_path}')
        
        
        
   
    
    def __traverse(self, base_dir):
        
        for (dirpath, dirnames, filenames) in os.walk(base_dir):
#            for filename in filenames:
#                
#                if filename == "tox.ini": 
#                    print(filename)
#                    self.__write_to_arr(os.path.normpath(os.path.join(base_dir, dirpath, filename)))
#                    pass
            
            for dirname in dirnames:
                if dirname == "tests":
                    test_path = os.path.join(dirpath, dirname)
                    
                    for (testdirpath, testdirnames, testfilenames) in os.walk(test_path):
                        for testfile in testfilenames:
                            self.__write_to_arr(os.path.normpath(os.path.join(test_path,testdirpath, testfile)))




    def get_files(self, base_dir):
        
        self.__traverse(base_dir)

#        self.__files["python"] = self.__python_files
        self.__files["yaml"] = self.__yaml_files
#        self.__files["tox"] = self.__tox_files
        
#        print (f'Pyhon files: {self.__files["python"]}')
#        print (f'\n ==\n Yaml files: {self.__files["yaml"]}')
#        print (f'\n == \n Tox files: {self.__files["tox"]}')
        
#        print(self.__files)
        return self.__files
    
    def get_playbook( yaml_file_path):
        with open(yaml_file_path, 'r') as f:
            try:
                playbook = yaml.load(f)
            except Exception as e:
                print (e)
                return None
        
        return playbook
    
    
    
    def get_tox_configs(tox_file_path):
        configs = configparser.ConfigParser()
        configs.read(tox_file_path)
        return configs
    
    def get_python_tokenized_file(filename):
        with tokenize.open(filename) as f:
            return ast.parse(f.read(), filename=filename)
    
        
    
    def write_to_file(self,anti_pattern_name, test_file_name, anti_pattern_count, project_name):
        print(f'{test_file_name} has {anti_pattern_name} upto {anti_pattern_count} times')
        headers = ['project_name','file_name','Skip_Ansible_Lint', 'Local_Only_Test', 'Assertion_Roulette', 'External_Dependency', 'No_ENV_CleanUp' ]
        outfile = project_name + "_output.csv"
        if path.exists(outfile) and (time.time() - os.path.getctime(outfile))<3600:
            print (f'appending in current output file')
            self.update_csv_line_panda(outfile,project_name, test_file_name, anti_pattern_name, anti_pattern_count)
            
                
        else:
            print("Creating a new csv file")
            try:
                self.__create_new_output_file(headers, outfile)
                self.update_csv_line_panda(outfile, project_name, test_file_name, anti_pattern_name, anti_pattern_count)
                
                
            except:
                print("Could not create output file")

        
        
    
    def __create_new_output_file(self, headers, filename):
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames = headers)
            csv_writer.writeheader()
            
        
    
    def is_substring( substrings, long_string):
        
        return any (sstr in long_string for sstr in substrings)
        
    def is_substring_v2( substrings, long_string):
        
#        print(f"long string:{long_string}")
        for substring in substrings:
            print(f"subsrting: {substring}")
            if substring in long_string:
                
                return True
        return False
#        
    def has_pattern_regex(pattern, long_string):
        return re.search(pattern, long_string) != None
        


    
    def __find_last_line_panda(self, file_name):
        df = pandas.read_csv(file_name)
        last_row = df.shape[0] - 1
        return df.loc[last_row, :]
    
    def update_csv_line_panda(self, output_file_name, project_name, test_file_name, column_name, new_value):
        df = pandas.read_csv(output_file_name, index_col='file_name')
        try:
            print(pandas.isnull(df.loc[test_file_name, column_name]))
            print("old line is being appended")
            df.at[test_file_name, column_name] = new_value
             
        except:
            print("new line is being created")
            
            df.loc[test_file_name, 'project_name'] = project_name
            df.at[test_file_name, 'Skip_Ansible_Lint'] = 0
            df.at[test_file_name, 'Local_Only_Test'] = 0
            df.at[test_file_name, 'Assertion_Roulette'] = 0
            df.at[test_file_name, 'External_Dependency'] = 0
            df.at[test_file_name, 'No_ENV_CleanUp'] = 0
            df.at[test_file_name, 'project_name'] = 0
            
            df.at[test_file_name, column_name] = new_value
#        df.at[test_file_name, column_name] = new_value
        df.to_csv(output_file_name)
        
    
## Tox automation detector
    def tox_commands_detector(configs):
        for config in configs.sections():
            print(f'\nsection name: {config}')
            for key in configs[config]:
                if key == 'commands':
                    print(configs[config][key])