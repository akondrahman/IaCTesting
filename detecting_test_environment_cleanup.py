#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tokenize
import ast


# In[11]:


def main():
    hasCleanup = has_clean_up_implementation('test_code_for_parsing.py')
    if hasCleanup:
        print ('This script has implemented clean up')
    else:
        print('No clean up found')


# In[12]:


def parse_file(filename):
    with tokenize.open(filename) as f:
        return ast.parse(f.read(), filename=filename)


# In[13]:


def has_clean_up_implementation(filename):
    
    for item in ast.walk(parse_file(filename)):
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = item.name
            if name.startswith(('tearDown', 'teardown', 'tear_down','cleanUp', 'cleanup', 'clean_up')) :
                return True
            
    return False


# In[14]:


print(has_clean_up_implementation('test_code_for_parsing.py'))


# In[15]:


if __name__ == "__main__":
    main()


# In[ ]:




