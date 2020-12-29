import logging, os
import pandas as pd
from shutil import copyfile
logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')

df = pd.read_csv(r'C:\mined_repos\file_list.csv')
dest_folder = r'C:\Mehedi\Bakups\oracle'
# print(df['file_name'])
for file_name in df['file_name']:
    # print(file)
    # print(os.path.exists(file))
    val = os.path.exists(file_name)
    
    if val == True:
        head, tail = os.path.split(file_name)
        project_name = file_name.split("\\")[2]
        # print(project_name)
        new_file_name = project_name + "_" + tail
        # print(head)
        # print(tail)
        print(new_file_name)
        copyfile(file_name,os.path.join(dest_folder,new_file_name))

        logging.debug("file %s is transferred as: %s", file_name,new_file_name)

    else:
        logging.debug("file %s could not be transferred as")


    