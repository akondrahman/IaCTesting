# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:40:31 2020

@author: mehedi.md.hasan
"""

from detectors.yaml_detectors.skip_linting_yaml_detector import SkipLintingYamlDetector
from detectors.yaml_detectors.localhost_testing_yaml_detector import LocalhostTestingYamlDetector
from detectors.yaml_detectors.assertion_roulette_yaml_detector import AssertionRouletteYamlDetector
from detectors.yaml_detectors.external_dependency_yaml_detector import ExternalDependencyYamlDetector
from detectors.yaml_detectors.test_env_not_cleaned_yaml_detector import TestEnvNotCleanedYamlDetector

from detectors.tox_detectors.external_dependency_tox_detector import ExternalDependencyToxDetector

from detectors.py_detectors.test_env_not_cleaned_python_detector import TestEnvNotCleanedPythonDetector
from detectors.py_detectors.external_dependency_python_detector import ExternalDependencyPythonDetector
from detectors.py_detectors.assertion_roulette_python_detector import AssertionRoulettePythonDetector


from util import Util

class IaCTestingAntipatterns:
    
    def __init__(self, files, project_name):
        self._project_name = project_name
        self.__files = files
        self.__skip_linting_yaml_detector = SkipLintingYamlDetector()
        self.__local_host_testing_yaml_detector = LocalhostTestingYamlDetector()
        self.__assertion_roulette_yaml_detector = AssertionRouletteYamlDetector()
        self.__external_dependency_yaml_detector = ExternalDependencyYamlDetector()
        self.__test_env_not_cleaned_yaml_detector = TestEnvNotCleanedYamlDetector()
        
        self.__external_dependency_tox_detector = ExternalDependencyToxDetector()
        
        self.__test_env_not_cleaned_python_detector = TestEnvNotCleanedPythonDetector()
        self.__external_dependency_python_detector = ExternalDependencyPythonDetector()
        self.__assertion_roulette_python_detector = AssertionRoulettePythonDetector()
    
    def get_anti_pattern_list(self):
        
#        python_files = self.__files['python']
        yaml_files = self.__files['yaml']
#        tox_files = self.__files['tox']
        
        for yaml_file in yaml_files:
            playbook = Util.get_playbook(yaml_file)
            
#            print(playbook)
            
            if playbook == None:
                continue
            
            self.__skip_linting_yaml_detector.detect_anti_pattern(playbook, yaml_file, self._project_name)
            self.__local_host_testing_yaml_detector.detect_anti_pattern(playbook, yaml_file, self._project_name)
            self.__assertion_roulette_yaml_detector.detect_anti_pattern(playbook, yaml_file, self._project_name)
            self.__external_dependency_yaml_detector.detect_anti_pattern(playbook, yaml_file, self._project_name)
            self.__test_env_not_cleaned_yaml_detector.detect_anti_pattern(playbook, yaml_file, self._project_name)
             
            
            
#        for tox_file in tox_files:
#            configs = Util.get_tox_configs(tox_file)
#            
#            self.__external_dependency_tox_detector.detect_anti_pattern(configs, tox_file, self._project_name)
        
        
#        for python_file in python_files:
#            parsed_file = Util.get_python_tokenized_file(python_file)
#            
#            self.__test_env_not_cleaned_python_detector.detect_anti_pattern(parsed_file, python_file, self._project_name)
#            self.__external_dependency_python_detector.detect_anti_pattern(parsed_file, python_file, self._project_name)
#            self.__assertion_roulette_python_detector.detect_anti_pattern(parsed_file, python_file, self._project_name)
        
    
    
    