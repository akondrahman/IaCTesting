# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:25:26 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector
from util import Util

class TestEnvNotCleanedYamlDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
    def __find_cleaned_up_roles(self, playbook):
        
        cleaned_up_roles = {}
        total_roles = []
        for role in playbook:
            try:
                role_vars = role['vars']
                for role_var in role_vars:
                    if self.__find_clean_up_var(role_var):
                        cleaned_up_roles['role_name'] = role['name']
                        cleaned_up_roles['var_name'] = role_var
                        total_roles.append(cleaned_up_roles)
                    
            except:
                continue

        
        return total_roles
    
    
    def __find_clean_up_var(self, long_string):
        clean_up_substrings = ['cleanup']
        return Util.is_substring(clean_up_substrings, long_string)


        
        
    
    def detect_anti_pattern(self, playbook, file_path):
        cleaned_up_roles = self.__find_cleaned_up_roles(playbook)
#        print(f'{file_path}====={tags}======')
        
        if len(cleaned_up_roles)<1:
#            print("Antipattern found")
#            print(f'boolean ==={self.__find_skip_lint()}====')
            self.__anti_pattern_count = 1
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "No_ENV_CleanUp"
            anti_pattern.path = file_path
            anti_pattern.antipattern_count = self.__anti_pattern_count
