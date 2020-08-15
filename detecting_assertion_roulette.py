#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
from pprint import pprint
import inspect
import astor


# In[67]:


def main():
    print(detectAssertionRoulette("test_code_for_parsing.py"))


# In[121]:


def detectAssertionRoulette(script_name):
# Defining Array to hold the function name, count of Assert statements & presence of smell
    fns = []

    #parsing the script using AST
    with open(script_name, "r") as source:
        tree = ast.parse(source.read())
        for block in tree.body:
            for node in ast.walk(block):
                fn = {}
                #checking whether current node is a function
                if isinstance(node, ast.FunctionDef):
                    fn['name'] = node.name
#                     fn['body'] = astor.to_source(node)
                    fn['countAssert'] = 0
                    fn['hasSmell'] = False
                    for body_item in node.body:
                        #checking if the function body has any assert statement
                        #and keeping the count of that
                        if isinstance(body_item, ast.Expr) :
                            ops = body_item.value.func.attr
                            if ops.startswith('assert'):
                                fn['countAssert'] = fn['countAssert'] + 1
                                
                                
                        #finding Assert inside a if condition of a With block
                        if isinstance(body_item, ast.With):
                            for with_body_item in body_item.body:
                                if isinstance( with_body_item, ast.If):
                                    if_with_body_items = with_body_item.body
                                    for if_with_body_item in if_with_body_items:
                                        ops2 = if_with_body_item.value.func.attr
                                        if ops2.startswith('assert'):
                                            fn['countAssert'] = fn['countAssert'] + 1
                                        
                                                                           
                        #finding plain Asserts        
                        if isinstance(body_item, ast.Assert):
                            fn['countAssert'] = fn['countAssert'] + 1            
                            
                    if fn['countAssert'] >1:
                        fn['hasSmell'] = True
                        
                        
                    fns.append(fn)
        return fns


# In[124]:


if __name__ == "__main__":
    main()


# In[ ]:


#https://stackoverflow.com/questions/54092879/how-to-find-out-if-the-source-code-of-a-function-contains-a-loop

