# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:03:20 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector
from util import Util


class ExternalDependencyToxDetector(AntiPatternDetector ):

    
    def __init__(self):
       
        self.__anti_pattern_count = 0

    def __find_external_dependency(self, configs):

        key_substrings = ['install', 'command', 'deps']
        external_dependencies = []
        
        
        for config in configs.sections():
            for key in configs[config]:
                if Util.is_substring(key_substrings, key):
#                    print("External Dependency Suspected...\n")
#                    print("...Checking for further artifacts...\n")
#                    print("...Value of the key is...\n")
#                    print(configs[config][key]+ "\n\n")
                    if self.__find_all_external_dependencies(str(configs[config][key])):
                        external_dependencies.append(config)
        
        self.__anti_pattern_count = len(external_dependencies)
        
        return external_dependencies
          
    
    
    def __find_all_external_dependencies(self, keyvalue):
        
        return self.__has_url_pattern(keyvalue) or self.__has_directory_pattern(keyvalue)
            
        
        
    
    
    def __has_url_pattern(self, url):
        url_substrings = ['http', 'https', 'sftp', 'ftp']
        
        return Util.is_substring(url_substrings, url)
    
    
    def __has_directory_pattern(self, path):
        
        dir_substrings = r'\/\w+\/'
        return Util.has_pattern_regex(dir_substrings, path)
        
            
       
    def detect_anti_pattern(self, configs, file_path, project_name):
        self.__anti_pattern_count = len(self.__find_external_dependency(configs))
        if (len(self.__find_external_dependency(configs))>0):
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "External_Dependency"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
