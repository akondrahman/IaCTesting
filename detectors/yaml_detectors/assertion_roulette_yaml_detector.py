# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:11:51 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector

class AssertionRouletteYamlDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
    
    def __find_assertion_roulette(self, playbook):
        
        has_assertion_roulette = False
        asserion_roulette_count = 0
        
        try:
           for pl in playbook:
                tasks = pl["tasks"]
                for task in tasks:
                    asserts = task['assert']['that']
                    if len(asserts) > 1:
                        
                        asserion_roulette_count += 1
        except Exception as e:
            # print("Ëntered in asserion_roulette_count except")
            # print(e)
            pass
        
        

        for roles in playbook:
            try:
                try:
                    tasks = roles['tasks']
                except:
                    tasks = roles['post_tasks']
                    for task in tasks:
                        asserts = task['assert']['that']
                        if len(asserts) > 1:
                            
                            asserion_roulette_count += 1
        
            except Exception as e:
                # print(e)
                pass
                
            try:
                asserts = roles['assert']['that']
                if len(asserts) > 1:
                    
                    asserion_roulette_count += 1
            
            except Exception as e:
                # print(e)
                continue
                
        
        return asserion_roulette_count
    
    
    
        
        
    
    def detect_anti_pattern(self, playbook, file_path, project_name):
        assrt_count = self.__find_assertion_roulette(playbook)
        self.__anti_pattern_count = assrt_count
        
        if (assrt_count>0):
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "Assertion_Roulette"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
            
