# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:47:13 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector

import ast

class TestEnvNotCleanedPythonDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
    def __find_clean_up_func(self, parsed_file):
        has_clean_up = False
        for item in ast.walk(parsed_file):
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                name = item.name
#                print(f'function_name is {name}')
                if name.startswith(('tearDown', 'teardown', 'tear_down','cleanUp', 'cleanup', 'clean_up')):
                    has_clean_up = True

        
        return has_clean_up
                    
                        
    
    def detect_anti_pattern(self, parsed_file, file_path, project_name):
        
        if not self.__find_clean_up_func(parsed_file):
#            print("Antipattern found")
#            print(f'boolean ==={self.__find_skip_lint()}====')
            self.__anti_pattern_count = 1
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "No_ENV_CleanUp"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
