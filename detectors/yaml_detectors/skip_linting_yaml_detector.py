# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:53:01 2020

@author: mehedi.md.hasan
"""


#from antipattern_detector import  AntiPatternDetector
from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector

class SkipLintingYamlDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
    def __find_tags(self, playbook):
        
        tags = []
        for role in playbook:
#            print(f'role name is {role}')
            try:
                try:
                    tasks = role['tasks']
                except:
                    tasks = role['post_tasks']
#                print(tasks)    
                for task in tasks:
#                    print(f'task name is {task}')
                    try:
                        tag_names = task['tags']
                        for tag_name in tag_names:
                            tags.append(tag_name)
                    except:
                        continue
            except:
                continue
        
        return tags
    
    
    
    def __find_skip_lint(self, tags):
        has_skip_linting = False
        for tag in tags:
            if tag == 'skip_ansible_lint':      
                has_skip_linting = True
                self.__anti_pattern_count +=1
        
        return has_skip_linting
    

        
        
    
    def detect_anti_pattern(self, playbook, file_path, project_name):
        tags = self.__find_tags(playbook)
#        print(f'{file_path}====={tags}======')
        
        if (self.__find_skip_lint(tags)):
#            print("Antipattern found")
#            print(f'boolean ==={self.__find_skip_lint()}====')
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "Skip_Ansible_Lint"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
            
        
        

  
        
    



            


