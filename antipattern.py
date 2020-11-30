# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:54:14 2020

@author: mehedi.md.hasan
"""

from abc import ABC, abstractmethod
from util import Util


class AntiPatternDetector(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def detect_anti_pattern(self, *args):
        pass
    

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
        self._project_name = None
        self._antipattern_count = 0
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def project_name(self):
        return self._project_name
    
    @property
    def path(self):
        return self._path
    @property
    def antipattern_count(self):
        return self._antipattern_count
    
    @name.setter
    
    def name (self, name):
        self._name = name
    
    @project_name.setter
    def project_name(self, project_name):
        self._project_name = project_name
        
    @path.setter
    def path(self, path):
        self._path = path
        
    
    @antipattern_count.setter
    def antipattern_count(self, antipattern_count):
        self._antipattern_count = antipattern_count
        self.notify_observer(self._name,self._path, self._antipattern_count, self._project_name)
        
        


class AntiPatternLogger(AntiPatternObserver):
    def write_anti_pattern_to_file(self, anti_pattern_name, file_path, antipattern_count, project_name):
        util_class = Util()
        util_class.write_to_file(anti_pattern_name, file_path, antipattern_count, project_name)