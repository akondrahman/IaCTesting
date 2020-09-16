# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:25:23 2020

@author: mehedi.md.hasan
"""

import yaml




def findHostType(playbook):
    
    taskNames = []
    
    for role in playbook:
        try:
            hostmapping = {}
            hosts = role['hosts']
            name = role['name']
            hostmapping['roleName'] = name
            hostmapping['hostName'] = hosts
            hostmapping['isLocalHost'] = False
            if hosts == 'localhost':
                hostmapping['isLocalHost'] = True
                
            taskNames.append(hostmapping)
            

        except:
            print("Task not found under this role")
    return taskNames

            




with open('test.yml', 'r') as f:
    playbook = yaml.load(f)


print(findHostType(playbook))

