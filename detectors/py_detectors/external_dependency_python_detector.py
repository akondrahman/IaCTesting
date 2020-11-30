# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:49:24 2020

@author: mehedi.md.hasan
"""


from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector
from util import Util
import ast

class ExternalDependencyPythonDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
   
    
    
    def __find_external_dependencies(self, file_path, parsed_file):
        external_dependencies = []
        
        with open(file_path) as my_file:
            for num, line in enumerate(my_file, 1):
                dependent_obj = {}
                
                if not line.lstrip().startswith('#') and self.__find_external_pattern(line):
#                    print(f'+++{line}+++')
                    func_name = self.__filename_and_lineno_to_def(parsed_file, num)
                    dependent_obj['file_name'] = file_path
                    dependent_obj['func_name'] = func_name
                    external_dependencies.append(dependent_obj)
        
#        print(f'===={external_dependencies}====')
        self.__anti_pattern_count = len(external_dependencies)
        
        return external_dependencies
        
    
    
    def __find_external_pattern(self, long_string):
        ### TODO: Need to add file import checks here

        lookups = ['path.join', 'http://', 'https://', 'open (', 'mysql', 'import_playbook']
        
        return Util.is_substring(lookups, long_string)
    
    
    def __filename_and_lineno_to_def(self, parsed_file, line_no):
        candidate = None
       
        for item in ast.walk(parsed_file):
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if item.lineno >line_no:
                    continue
                if candidate:
                    distance = line_no - item.lineno
                    
                    if distance < (line_no - candidate.lineno):
                        candidate = item
                else:
                    candidate = item
        
        if candidate:
           return candidate.name
    
           
        
    
    def detect_anti_pattern(self, parsed_file, file_path, project_name):
        
        if len(self.__find_external_dependencies(file_path, parsed_file))>0:
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "External_Dependency"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
            


