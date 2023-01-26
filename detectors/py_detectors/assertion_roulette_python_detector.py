# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:20:43 2020

@author: mehedi.md.hasan
"""

from antipattern import AntiPattern, AntiPatternLogger, AntiPatternDetector
import ast

class AssertionRoulettePythonDetector(AntiPatternDetector ):
    
    def __init__(self):
       
        self.__anti_pattern_count = 0
        
    
    def __finding_functions_with_assertion_roulette(self, file_path):
        fns = []
        
        with open(file_path, "r") as source:
            tree = ast.parse(source.read())
            
            for block in tree.body:
                for node in ast.walk(block):
                    fn = {}
                    
                    if isinstance(node, ast.FunctionDef):
                        fn['name'] = node.name
                        fn['assert_count'] = 0
                        
                        for body_item in node.body:
                        #checking if the function body has any assert statement
                        #and keeping the count of that
                            
                            if isinstance(body_item, ast.Expr) :
                                try:
                                    ops = body_item.value.func.attr
                                    if ops.startswith('assert'):
                                        fn['assert_count'] +=1
                                except:
                                    pass
                        
                        #finding Assert inside a if condition of a With block
                            
                            if isinstance(body_item, ast.With):
                                for with_body_item in body_item.body:
                                    if isinstance (with_body_item, ast.If):
                                        if_with_body_items = with_body_item.body
                                        for if_with_body_item in if_with_body_items:
                                            try:
                                                ops2 = if_with_body_item.value.func.attr
                                                if ops2.startsWith('assert'):
                                                    fn['assert_count'] +=1
                                            except:
                                                pass
                            
                            #finding plain Asserts  
                            
                            if isinstance(body_item, ast.Assert):
                                fn['assert_count'] += 1
                            
                            print(fn)
                            
                        if fn['assert_count'] > 1:
#                            print(fn)
                            fns.append(fn)
        
        return fns
    
    
    def __find_assertion_roulette(self, file_path):
        fns = self.__finding_functions_with_assertion_roulette(file_path)
        
        self.__anti_pattern_count = len(fns)
        
        if  self.__anti_pattern_count > 0:
            return True
        else:
            return False
                                
      
    
    def detect_anti_pattern(self, parsed_file, file_path, project_name):
            
        if (self.__find_assertion_roulette(file_path)):
            anti_pattern = AntiPattern()
            antipattern_logger = AntiPatternLogger()
            anti_pattern.add_observer(antipattern_logger)
            anti_pattern.name = "Assertion_Roulette"
            anti_pattern.path = file_path
            anti_pattern.project_name = project_name
            anti_pattern.antipattern_count = self.__anti_pattern_count
            
