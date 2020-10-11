# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:49:15 2020

@author: mehedi.md.hasan
import, var_files,pip_install_upper_constraints_proto 

"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector
from util import Util

class ExternalDependencyYamlDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
    def __find_roles_using_import(self, playbook):
        
        imported_roles = []
        
        for roles in playbook:
            try:
                imported_roles.append(roles['import_playbook'])
            except:
                continue
            
        
        return imported_roles
    
    
    
    
    
    def __find_roles_using_url(self, playbook):
        url_roles = []
        
        for roles in playbook:
            try:
                role_vars = roles['vars']
                
                for role_var in role_vars:
                    role_var_value = role_vars[role_var]
#                    print("==Entered Here==")
#                    print(role_var_value)
#                    print("==Exited from here==")
                    found_url = self.__find_url_in_string(role_var_value)
                    if found_url:
                        url_roles.append(roles['name'])
            except:
                continue
        return url_roles
    
    
    
    def __find_url_in_string(self, long_string):
        url_strings = ['http', 'https']
        if Util.is_substring(url_strings, long_string):
            
            return True
        else:
            return False
    
    # TODO: Need to add url detection
    
    def __find_external_dependency(self, playbook):
        imported_roles = self.__find_roles_using_import(playbook)
#        url_roles = self.__find_roles_using_url(playbook)
        
#        
        if len(imported_roles)>0  :
            self.__anti_pattern_count = len (imported_roles)
            return True
        else:
            return False
    
    
    
    
       
        
    
    def detect_anti_pattern(self, playbook, file_path):
        
        if (self.__find_external_dependency(playbook)):
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "External_Dependency"
            anti_pattern.path = file_path
            anti_pattern.antipattern_count= self.__anti_pattern_count
            
