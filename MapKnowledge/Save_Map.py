import json

class save_map():
    def __init__(self):
        #self.map = map
        pass
    def save_map(self,mapName):
        data = {}   
        data['key']='value'
        self.writeToJSONFile('./Data/',mapName,data)

    def writeToJSONFile(self,path,fileName,data):
        filePathNameWExt = './Data/' + fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data,fp)
        