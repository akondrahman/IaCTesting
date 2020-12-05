import http.client, os, git, shutil,stat
from os import path
import requests, json
from datetime import datetime
import gitlab

def searchGitlab():
    # url = "https://gitlab.com/api/v4/search?page="+page_number+"&per_page="+per_page+"&scope=projects&search=ansible"
    # payload={}
    # headers = {
    #     'PRIVATE-TOKEN': 'ym_J9_F6GBXf4yF2ToQs'
    #     }

    # response = requests.request("GET", url, headers=headers, data=payload)
    # res_data = json.loads(response.text)
    # res_header = response.headers
    # print(res_header["Link"])

    gl = gitlab.Gitlab('https://gitlab.com', private_token='ym_J9_F6GBXf4yF2ToQs')
    srch_result = gl.search('project', 'ansible')

    for item in srch_result:
        print(item)



searchGitlab()


    
