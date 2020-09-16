from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import yaml


# In[83]:
def getCoef(taskCoefficient):
    return taskCoefficient['coeff']


def consolidateTaskNames(playbook):
    stringsToVerify = ['verify', 'check', 'assert', 'ensure']
    taskNames = []
    taskNamesVerify = []
    totalTasks = {}

    
    for role in playbook:
        try:
            tasks = role['tasks']
            for task in tasks:
                taskNames.append(task['name'])
                res = any(ele in str(task['name']).lower()                           for ele in stringsToVerify) 
                if(res):
                    taskNamesVerify.append(task['name'])        
        
        except:
            print("task not found under this role: " + role['name'])
    
    totalTasks['tasks'] = taskNames
    totalTasks['verifierTasks'] = taskNamesVerify
    
    return totalTasks





def returnCosineSimilarity(str1, str2):
    str1List = word_tokenize(str1)
    str2List = word_tokenize(str2)
    sw = stopwords.words('english')
    l1 = []
    l2 = []
    # remove stop words from the string 
    str1Set = {w for w in str1List if not w in sw}  
    str2Set = {w for w in str2List if not w in sw}
    # form a set containing keywords of both strings  
    rvector = str1Set.union(str2Set)  
    for w in rvector: 
        if w in str1Set: 
            l1.append(1) # create a vector 
        else: 
            l1.append(0) 
        if w in str2Set:
            l2.append(1) 
        else:
            l2.append(0) 
    c = 0
  
# cosine formula  
    for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 

    return cosine



def findTheBestMatchingTask(verifierTask, allTasks):
    taskCoefficients = []
    for task in allTasks:
        namedList = {}
        coeff = returnCosineSimilarity(str(task).lower(), str(verifierTask).lower())
        if coeff < 1:
            namedList['taskName'] = task
            namedList['coeff'] = coeff
            taskCoefficients.append(namedList)
    
    taskCoefficients.sort(key = getCoef, reverse = True)
#     print(taskCoefficients)
    
    return taskCoefficients[0]



with open('test.yml', 'r') as f:
    playbook = yaml.load(f)

tasks = consolidateTaskNames(playbook)
verifierTasks = tasks['verifierTasks']
allTasks = tasks['tasks']

# print(verifierTasks)
taskCombo = []

for verifierTask in verifierTasks:
    taskPair = {}
#     print(verifierTask)
    bestMatch = findTheBestMatchingTask (verifierTask, allTasks)
    taskPair['preperationTask'] = bestMatch['taskName']
    taskPair['verifierTask'] = verifierTask
    taskCombo.append(taskPair)
    
print(taskCombo)