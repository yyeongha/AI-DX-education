# import lib
import os
import shutil
from datetime import datetime

# calculater today's date
now_date = datetime.today().strftime("%Y%m%d%H%M%S")
# print(now_date)

os.rename('./dataset', f'./dataset_{now_date}')

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
# print(file_list)

dataset_labels = {}

# keeping previous data
os.rename('./dataset', f'./dataset_{now_date}')

# making dataset
# making dataset directory 
createFolder("./dataset")

# generating file
save_file = open('./dataset/labels.txt', 'w', encoding='utf8')

# generating dataset object directory
for file in file_list:
    # print(file)
    # seperating sentence
    sp_file = file.split('_')
    print("순번: ",sp_file[0])
    print("한글이름: ",sp_file[1])
    print("영문이름: ",sp_file[2])
    
    # create folder
    createFolder(f"./dataset/{sp_file[2]}")
    
    # making label
    dataset_labels[sp_file[2]] = sp_file[1]
    print(f'{sp_file[2]}, {sp_file[1]}', file=save_file)
    
# dataset dictionary
print(dataset_labels)

save_file.close()

# 원본파일을 dataset에 처리하는 함수
org_path = "./org_data"
file_list = os.listdir(org_path)
for dir in file_list:
    files = os.listdir(org_path + f'./{dir}')
    print('*'*50)
    print(dir)
    print('*'*50)
    print(files)
        
    
    
    
    