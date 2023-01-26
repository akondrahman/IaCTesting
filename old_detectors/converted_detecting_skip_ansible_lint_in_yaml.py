# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:25:23 2020

@author: mehedi.md.hasan
"""

import yaml

def main():
    with open('test.yml', 'r') as f:
        playbook = yaml.load(f)
    tags = findTags(playbook)
    if (findSkipLint(tags)):
        print("Linting has been skipped")
    else:
        print("No skip linting has been found")


def findTags(playbook):
    
    tags = []      
    
    for role in playbook:
        try:
            try:
                tasks = role['tasks']
            except:
                tasks = role ['post_tasks']

            for task in tasks:
#                    print(task)
                    try:
                        tagNames = task['tags']
                        for tagName in tagNames:
                            tags.append(tagName)
                    except:
                        continue
    
        except:
            print("Task not found under this role")
    
    
    return tags

            


def findSkipLint(tags):
    
    for tag in tags:
        if tag == 'skip_ansible_lint':      
            return 1
    
    return 0

if __name__ == "__main__":
    main()
