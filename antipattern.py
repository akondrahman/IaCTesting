# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:54:14 2020

@author: mehedi.md.hasan
"""

from abc import ABC, abstractmethod
from util import Util

class AntiPatternObserver(ABC):
    @abstractmethod
    def write_anti_pattern_to_file(self, *args):
        pass
    
    
class AntiPatternObservable():
    
    def __init__(self):
        self.__observers = []
    
    def add_observer(self, oberver):
        self.__observers.append(oberver)
#        print("Observer has been added")
    
#    def delete_observer(self, observer):
#        self.__observers.remove(observer)
        
    def notify_observer(self, *args):
#        print("Observer has been notified")
        for observer in self.__observers:
            observer.write_anti_pattern_to_file( *args)
            

class AntiPattern(AntiPatternObservable):
    
    
    def __init__(self):
        super().__init__()
        self._name = None
        self._path = None
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def path(self):
        return self._path
    
    @name.setter
    
    def name (self, name):
        self._name = name
        
    @path.setter
    def path(self, path):
        self._path = path
        self.notify_observer(self._name,self._path)
        


class AntiPatternLogger(AntiPatternObserver):
        def write_anti_pattern_to_file(self, anti_pattern_name, file_path):
            Util.write_to_file(anti_pattern_name, file_path)