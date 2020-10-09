# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:11:51 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector

class AssertionRouletteYamlDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__has_anti_pattern = 0
    
    def __find_assertion_roulette(self, playbook):
        
        has_assertion_roulette = False
        
        for roles in playbook:
            try:
                try:
                    tasks = roles['tasks']
                except:
                    tasks = roles['post_tasks']
                    for task in tasks:
                        asserts = task['assert']['that']
                        if len(asserts) > 1:
                            has_assertion_roulette = True
        
            except:
                continue
            
        
        return has_assertion_roulette
    
    
    
        
        
    
    def detect_anti_pattern(self, playbook, file_path):
            
        if (self.__find_assertion_roulette(playbook)):
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "Assertion_Roulette"
            anti_pattern.path = file_path
            
