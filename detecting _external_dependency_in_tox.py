# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:03:46 2020

@author: mehedi.md.hasan
"""

import configparser
import re

def main():
    configs = configparser.ConfigParser()
    configs.read('tox.ini')
    
    hasExternalDependency = hasExternalDependencyInTox(configs)
    
    if(hasExternalDependency):
        print("Code has external dependency")





#print(configs.sections())
def hasExternalDependencyInTox(configs):
    hasDependency = False
    keySubstrings = ['install', 'command', 'deps']
#    valueSubstrings = ['https', 'http']
    for config in configs.sections():
        print(config)
        for key in configs[config]:
            print("\t" + "keyName: " + key)
            if (any([substring in key for substring in keySubstrings])):
                print("External Dependency Suspected...\n")
                print("...Checking for further artifacts...\n")
                print("...Value of the key is...\n")
                print(configs[config][key]+ "\n\n")
                if findExternalDependency(str(configs[config][key])):
                    print("External Dependency Found")
                    hasDependency = True
    
    return hasDependency



def findingDirectoryPattern(dir1):
    if re.search(r'\/\w+\/', dir1) == None:
        print("\n... file directory pattern found...\n")
        return False
    else:
        return True


def findUrlPattern(url):
    valueSubstrings = ['https', 'http', 'sftp', 'ftp']
    if (any([substring in url for substring in valueSubstrings])):
        print("\n... external url pattern found...\n")
        return True
    else:
        return False
    

def findExternalDependency(pattern):
    if findingDirectoryPattern(pattern) or findUrlPattern(pattern):
        return True
    else:
        return False
    

if __name__ == "__main__":
    main()
            

