import pickle 

pFile = open('pFile.pickle', 'wb') # b = binary

saveData = {
    "name" : "홍길동",
    "age" : 35,
    "lang" : "python"
}

pickle.dump(saveData, pFile)

pFile.close()
