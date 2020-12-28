with open(r'C:\mined_repos\file_list.csv') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
