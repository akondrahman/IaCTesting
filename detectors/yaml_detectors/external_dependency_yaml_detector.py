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
    
    
    
    
    
    def __find_roles_using_url(self, file_path):
        no_url = 0
        s = "http"
        with open(file_path) as f:
            for ll in f:
                if not ll.startswith("#"):
                    status = s in ll
                    # print (status)
                    if status == True:
                        no_url += 1
        
        return no_url


    
    
    
    
    # TODO: Need to add url detection
    
    def __find_external_dependency(self, playbook, file_path):
        imported_roles = self.__find_roles_using_import(playbook)
        url_roles = self.__find_roles_using_url(file_path)
        
#        
        if len(imported_roles)>0 or url_roles>0  :
            self.__anti_pattern_count = len (imported_roles) + url_roles
            return True
        else:
            return False
    
    
    
    
       
        
    
    def detect_anti_pattern(self, playbook, file_path, project_name):
        
        if (self.__find_external_dependency(playbook, file_path)):
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "External_Dependency"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count= self.__anti_pattern_count
            
