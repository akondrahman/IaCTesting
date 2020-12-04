import git, pymysql, os, logging
logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

#set GIT_PYTHON_GIT_EXECUTABLE=C:\Program Files\Git\cmd\git.exe
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()

def get_all_gitlab_repo_id():
   
    try:
        cursor.execute('select * from final_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows




def download_repo(ext_dir, repo):
    logging.error('starting to download repo no %s named %s' , repo[0], repo[1])
    base_repo = repo[1].split("/")[1]
    writer = repo[1].split("/")[0]
    repo_dir = ext_dir+"\\"+writer
    full_dir = ext_dir+"\\"+writer+"_"+base_repo
    try:
        os.mkdir(repo_dir)
    except:
        logging.error("Could not create any directory named %s", repo_dir)
    repo_url = repo[2]
    try:
        git.Git(repo_dir).clone(repo_url)
        logging.error('completed the download of repo %s', repo[0])
        return True
       
    except Exception as e:
        logging.error(e)
        if (os.path.exists(full_dir)):
            return True
        else:
            return False
   
# def delete_repo(full_dir):
#     print(f"deleting the directory: {full_dir}")
#     print("=================")
#     for root, dirs, files in os.walk(full_dir):
#         for dir in dirs:
#             os.chmod(path.join(root, dir), stat.S_IRWXU)
#         for file in files:
#             os.chmod(path.join(root, file), stat.S_IRWXU)
   
#     try:
#         shutil.rmtree(full_dir)
#         print("deletion completed")
#         print("=================")

#     except Exception as e:
#         print(e)
       
   



       

   
ext_dir = r'C:\mined_repos'
# repo_name = 'jpbarto/cicd_tf_workshop'
#repo_type = 1
#find_iac_percentage(repo_name, ext_dir, repo_type)
# download_repo(ext_dir, repo_name)

repos = get_all_gitlab_repo_id()

for repo in repos:
    print (f'\n ====Repo ID is {repo[0]}\n\n ====')
    download_repo(ext_dir, repo)
    
        
