import os
path , all = input() , []
os.chdir(path)
dirs = os.listdir(path)

print("All directories and files : " , *[x for x in dirs] , sep='\n')
print("Only directories: ", *[x for x in dirs if os.path.isdir(x)], sep='\n')
print("Only files: ", *[x for x in dirs if os.path.isfile(x)], sep = '\n')



