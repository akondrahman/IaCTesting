# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:26:12 2020

@author: mehedi.md.hasan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:25:23 2020

@author: mehedi.md.hasan
"""

import yaml


def main():
    with open('test.yml', 'r') as f:
        playbook = yaml.load(f)
    
#    print(playbook)
    
    cleanUps = findCleanUp(playbook)
    if len(cleanUps) > 0 :
        print("Environment has been cleaned up at least once")
    else:
        print("Environment has not been cleaned up in any task")

    
def findCleanUp(playbook):
    
    cleanedUpRoles = {}
    totalRoles = []
    cleanUpSubstrings = ['cleanup']

    for role in playbook:
        roleVars = role['vars']
        
        for roleVar in roleVars:
            if (any([substring in roleVar for substring in cleanUpSubstrings])):
            
#                print("Cleaning Up: " + roleVar)
                cleanedUpRoles['roleName'] = role['name']
                cleanedUpRoles['varName'] = roleVar
                totalRoles.append(cleanedUpRoles)
                
                
    
    return totalRoles



if __name__ == "__main__":
    main()