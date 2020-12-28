import os



def find_test_folders(base_dir):
    target_folder = "\\test"    
    for (dirpath, dirnames, filenames) in os.walk(base_dir):
        for file in filenames:
            
            if not target_folder in dirpath:
                print("Target folder not found in")
                file_path = os.path.join(dirpath, file)
                print(file_path)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(e)
                    continue
      
    # print(f'yml file count:{yml_counter}')
    
    # return  yml_counter
# count_test_files(r"C:\mined_repos\guardianproject-ops")


base_dir = r"C:\mined_repos\skyscape-cloud-services"
find_test_folders(base_dir)