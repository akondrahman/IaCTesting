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
    
    