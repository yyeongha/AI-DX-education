fileload = open('save.txt','r', encoding='utf8')

# print(fileload)

while True:
    line = fileload.readline()

    if not line:
        break
    print(line, end='')
    
fileload.close()