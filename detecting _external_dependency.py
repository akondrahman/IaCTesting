#!/usr/bin/env python
# coding: utf-8

# In[99]:


import tokenize
import ast

def parse_file(filename):
    with tokenize.open(filename) as f:
        return ast.parse(f.read(), filename=filename)


# In[100]:



def filename_and_lineno_to_def(filename, lineno):
    candidate = None
    for item in ast.walk(parse_file(filename)):
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
         
            if item.lineno > lineno:
                # Ignore whatever is after our line
                continue
            if candidate:
                distance = lineno - item.lineno
                if distance < (lineno - candidate.lineno):
                    candidate = item
#                     print(candidate.name)
            else:
                candidate = item

    if candidate:
        return candidate.name


# In[95]:


def detectExternalDependency(filename):
    #keywords which have been observed in the sample code 
    lookups = ['path.join', 'http://', 'https://', 'open (', 'mysql']
    
    externalDependencies = []
    

    with open(filename) as myFile :
        for num, line in enumerate(myFile, 1):
            dependentObj = {}
            
            for lookup in lookups:
                if lookup in line:
                    funcName = filename_and_lineno_to_def(filename, num)
                    dependentObj['filename'] = filename
                    dependentObj['functionName'] = funcName
                    dependentObj['lineNo'] = num
                    externalDependencies.append(dependentObj)
    
        
    return externalDependencies


# In[103]:


print(detectExternalDependency('test_code_for_parsing.py'))


# In[ ]:




