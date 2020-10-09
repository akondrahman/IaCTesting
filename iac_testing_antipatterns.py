# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:40:31 2020

@author: mehedi.md.hasan
"""

from detectors.yaml_detectors.skip_linting_yaml_detector import SkipLintingYamlDetector
from detectors.yaml_detectors.localhost_testing_yaml_detector import LocalhostTestingYamlDetector
from detectors.yaml_detectors.assertion_roulette_yaml_detector import AssertionRouletteYamlDetector
from detectors.yaml_detectors.external_dependency_yaml_detector import ExternalDependencyYamlDetector

from util import Util

class IaCTestingAntipatterns:
    
    def __init__(self, files):
        self.__files = files
        self.__skip_linting_yaml_detector = SkipLintingYamlDetector()
        self.__local_host_testing_yaml_detector = LocalhostTestingYamlDetector()
        self.__assertion_roulette_yaml_detector = AssertionRouletteYamlDetector()
        self.__external_dependency_yaml_detector = ExternalDependencyYamlDetector()

        
    
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
            self.__local_host_testing_yaml_detector.detect_anti_pattern(playbook, yaml_file)
            self.__assertion_roulette_yaml_detector.detect_anti_pattern(playbook, yaml_file)
            self.__external_dependency_yaml_detector.detect_anti_pattern(playbook, yaml_file)
             
            
            
            
            
        
    
    
    