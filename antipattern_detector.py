# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:43:03 2020

@author: mehedi.md.hasan
"""
from abc import ABC, abstractmethod

class AntiPatternDetector(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def detect_anti_pattern(self, *args):
        pass
    
#    @abstractmethod
#    def update_anti_pattern_list(self, *args):
#        pass

#class AntiPatternDetectorObservable():
#    
#    def __init__(self):
#        self.__observers = []
#    
#    def add_observer(self, observer):
#        self.__observers.append(observer)
#    
#    def notify_observer(self, *args):
#        for observer in self.__observers:
#            observer.update(self, *args)
            
        
    