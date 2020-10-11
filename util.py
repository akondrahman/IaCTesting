# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:13:49 2020

@author: mehedi.md.hasan
import, var_files,pip_install_upper_constraints_proto 

"""
import os, yaml, re, configparser, ast, tokenize

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
    
        
    
    def write_to_file( anti_pattern_name, filepath, antipattern_count):
        print(f'{filepath} has {antipattern_count} no of suspected {anti_pattern_name}  antipattern of IaC Testing')
        
    
    def is_substring( substrings, long_string):
        
        return any (sstr in long_string for sstr in substrings)
        
#        for substring in substrings:
#            if substring in long_string:
#                return True
#        return False
#        
    def has_pattern_regex(pattern, long_string):
        return re.search(pattern, long_string) != None
        
