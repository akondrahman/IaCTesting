# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 23:37:07 2020

@author: mehedi.md.hasan
"""
import yaml

def main():
    with open('test.yml', 'r') as f:
        playbook = yaml.load(f)
    
    if (findAssertionRoulette(playbook)):
        print("Assertion Roulette found")
    else:
        print("No Assertion Roulette found")

def findAssertionRoulette(playbook):
    assertionRoulette = 0
    for roles in playbook:
        try:
            try:
                tasks = roles['tasks']
            except:
                tasks = roles['post_tasks']
            for task in tasks:
                asserts = task['assert']['that']
                if len(asserts) > 1:
                    assertionRoulette = 1
        
        except:
            print("No task found under this role")
        
    return assertionRoulette

