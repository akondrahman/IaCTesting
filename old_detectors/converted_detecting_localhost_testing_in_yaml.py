# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:25:23 2020

@author: mehedi.md.hasan
"""

import yaml


def main():
    with open('test.yml', 'r') as f:
        playbook = yaml.load(f)
    
    testEnvironments = findHostType(playbook)
#    print (testEnvironments)

    if len(testEnvironments['remote']) < 1:
        print("No remote Test Has been found")
    
    
def findHostType(playbook):
    
    roleNames = {}
    localTestRoles = []
    remoteTestRoles = []
    
    for role in playbook:
        try:
            hostmapping = {}
            hosts = role['hosts']
            name = role['name']
            hostmapping['roleName'] = name
            hostmapping['hostName'] = hosts

            if hosts == 'localhost':
                hostmapping['isLocalHost'] = 1
                
                
                try:
                    tasks = role['tasks']
                except:
                    tasks = role ['post_tasks']
                    
                taskNames = []
                for task in tasks:
                    taskNames.append(task['name'])
                    
                hostmapping['taskNames'] = taskNames
                localTestRoles.append(hostmapping)
                    
            else :
                hostmapping['isLocalHost'] = 0
                
                try:
                    tasks = role['tasks']
                except:
                    tasks = role ['post_tasks']
                
                taskNames = []
                for task in tasks:
                    taskNames.append(task['name'])
                
                hostmapping['taskNames'] = taskNames
                remoteTestRoles.append(hostmapping)
                

            

        except:
            print("Task not found under this role")
    
    roleNames['local'] = localTestRoles
    roleNames['remote'] = remoteTestRoles
    
    return roleNames

            



if __name__ == "__main__":
    main()