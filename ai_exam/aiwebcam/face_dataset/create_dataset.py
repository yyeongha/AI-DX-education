# import lib
import os
import shutil

# directory generating function
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("에러 : 디렉토리 생성에러. " + directory)
        
# function that import file to original directory
org_path = "./org_data"
file_list = os.listdir(org_path)
print(file_list)

# making dataset
# making dataset directory 
createFolder("./dataset")


