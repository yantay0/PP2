from  os import access  ,  chdir , F_OK , W_OK , X_OK , R_OK
path=input()
chdir(path)
print("Accessed" if access(path, F_OK) else "No Access")  # os.F_OK - объект существует,
print("Object is Readble !" if access(path, R_OK) else "Error")
print("Object is Writable !" if access(path, W_OK) else "Error")  
print("Object is Executable !" if access(path, X_OK) else "Error")


