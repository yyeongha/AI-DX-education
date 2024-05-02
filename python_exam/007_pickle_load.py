import pickle

loadFile = open('pFile.pickle', 'rb')

memData = pickle.load(loadFile)

print(memData)

loadFile.close()