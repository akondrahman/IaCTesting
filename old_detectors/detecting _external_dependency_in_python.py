#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tokenize
import ast


# In[26]:


def main():
    dependencies = detectExternalDependency('test_code_for_parsing.py')
#     dependencies = []
    
    if len(dependencies) == 0:
        print("No external dependency found")
        return 0
    else :
        print("Some external dependencies has been identified. Please check the following line numbers")
        
        for dependency in dependencies:
            print(dependency['lineNo'] )
            


# In[27]:


def parse_file(filename):
    with tokenize.open(filename) as f:
        return ast.parse(f.read(), filename=filename)


# In[28]:



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


# In[33]:


def detectExternalDependency(filename):
    #keywords which have been observed in the sample code 
    lookups = ['path.join', 'http://', 'https://', 'open (', 'mysql', 'import_playbook']
    
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


# In[34]:


print(detectExternalDependency('test_code_for_parsing.py'))


# In[35]:


if __name__ == "__main__":
    main()


# In[ ]:




