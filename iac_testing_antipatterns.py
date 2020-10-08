# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:40:31 2020

@author: mehedi.md.hasan
"""

from skip_linting_yaml_detector import SkipLintingYamlDetector
from util import Util

class IaCTestingAntipatterns:
    
    def __init__(self, files):
        self.__files = files
        self.__skip_linting_yaml_detector = SkipLintingYamlDetector()

        
    
    def get_anti_pattern_list(self):
        
#        python_files = files['python']
        yaml_files = self.__files['yaml']
#        print(yaml_files)
#        tox_files = files['tox']
        
        for yaml_file in yaml_files:
            playbook = Util.get_playbook(yaml_file)
            
#            print(playbook)
            
            if playbook == None:
                continue
            
            self.__skip_linting_yaml_detector.detect_anti_pattern(playbook, yaml_file)
             
            
            
            
            
        
    
    
    