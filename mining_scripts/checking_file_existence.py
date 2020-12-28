import logging, os
import pandas as pd
logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')

df = pd.read_csv(r'C:\mined_repos\file_list.csv')
# print(df['file_name'])
for file in df['file_name']:
    # print(file)
    # print(os.path.exists(file))
    val = os.path.exists(file)
    logging.debug("file %s is found: %s", file,val)

    