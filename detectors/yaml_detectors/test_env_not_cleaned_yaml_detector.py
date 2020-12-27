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
        self.__file_path = None
    
    def __find_cleaned_up_roles(self, playbook):
        
        total_installation_tasks = 0
        total_cleanup_tasks = 0     
        
        try:
           for pl in playbook:
                tasks = pl["tasks"]
                for task in tasks:
                    task_name = task['name']
                    print(f'task name without role is {task_name}')
                    if self.__check_installation_task(task_name):
                        print(f'task name without is {task_name} has installation')
                        total_installation_tasks += 1
                    if self.__check_clean_up_task(task_name):
                        print(f'task name is {task_name} has removal')
                        total_cleanup_tasks += 1
        except:
            pass
#          
        
        for role in playbook:
                                   
            try:
                try:
                    tasks = role['tasks']
                except:
                    tasks = role['post_tasks']
                    for task in tasks:
                        task_name = task['name']
                        print(f'task name is {task_name}')
                            
                        if self.__check_installation_task(task_name):
                            print(f'task name is {task_name} has installation')
                            total_installation_tasks += 1
                        if self.__check_clean_up_task(task_name):
                            print(f'task name is {task_name} has removal')
                            total_cleanup_tasks += 1

            except:
                continue
            print(f"{self.__file_path} has total installation count {total_installation_tasks}")
            print(f"{self.__file_path} has total removal count {total_cleanup_tasks}")
                
            if total_installation_tasks > 0 and total_cleanup_tasks < 1:
                return total_installation_tasks
            if total_installation_tasks > 0 and total_cleanup_tasks > 0:
                return (total_installation_tasks - total_cleanup_tasks)
            

        
        return total_installation_tasks
    
    def __check_installation_task(self, task_name):
        installation_subscrings = ['install', 'installation', 'Install', 'Installation']
        res = Util.is_substring_v2(installation_subscrings, task_name)
        print(f'{task_name} installation check result is {res}')
        return Util.is_substring_v2(installation_subscrings, task_name)
        

    
    def __check_clean_up_task(self, task_name):
        clean_up_subscrings = ['uninstall','clean', 'teardown', 'cleanup', 'cleanUp', 'remove']
        return Util.is_substring_v2(clean_up_subscrings, task_name)
        
        
    
    def detect_anti_pattern(self, playbook, file_path, project_name):
        self.__file_path = file_path
        cleaned_up_roles = self.__find_cleaned_up_roles(playbook)
#        print(f'{file_path}====={tags}======')
        
        if cleaned_up_roles>0:
#            print("Antipattern found")
#            print(f'boolean ==={self.__find_skip_lint()}====')
            self.__anti_pattern_count = cleaned_up_roles
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "No_ENV_CleanUp"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
