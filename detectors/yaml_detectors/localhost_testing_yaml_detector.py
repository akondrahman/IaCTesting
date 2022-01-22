# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:57:31 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector

class LocalhostTestingYamlDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
    def __find_host_type(self, playbook):
        
        role_names = {}
        local_test_roles = []
        remote_test_roles = []
        
        for role in playbook:
            # print(f'role name is {role}')
            try:
                hostmapping = {}
#                hostmapping['role_name'] = role['name']
                hostmapping ['host_name'] = role['hosts']
                
                if hostmapping ['host_name'] == 'localhost':
                    hostmapping['is_local_host'] = 1
                    local_test_roles.append(hostmapping)
                    
                else:
                    hostmapping['is_local_host'] = 0
                    remote_test_roles.append(hostmapping)
            except Exception as e:
                # print("Entered in the localhost try catch")
                # print(e)
                continue
        
        role_names['local'] = local_test_roles
        role_names['remote'] = remote_test_roles
            
        print(role_names)
        return role_names
    
    
    
    def __find_local_only_test(self, role_names):
        
        
       if len(role_names['remote'])< 1:
           self.__anti_pattern_count = len(role_names['local'])
           return 1
       else:
           return 0

        
        
    
    def detect_anti_pattern(self, playbook, file_path, project_name):
        role_names = self.__find_host_type(playbook)
#        print(f'{file_path}====={tags}======')
        
        if (self.__find_local_only_test(role_names) == 1):
#            print("Antipattern found")
#            print(f'boolean ==={self.__find_skip_lint()}====')
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "Local_Only_Test"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
            
