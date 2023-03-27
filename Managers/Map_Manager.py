#this manager saves and loads map data
#late on it may look at the active map, but it doesn't do that yet
import json

class map_manager():
    def __init__(self,map_name):
        self.map_name = map_name
    
    def on_step():
        pass

    def load_map(self):
        #if not file_name exists:
        #   return False
        #else: 
        #map = readfile(map)
        if not 
        pass

    def save_map(self,map_name):
        data = {}   
        data['key']='value'
        self.writeToJSONFile('./Data/',map_name,data)
        def writeToJSONFile(self,path,fileName,data):
            filePathNameWExt = './Data/' + fileName + '.json'
            with open(filePathNameWExt, 'w') as fp:
                json.dump(data,fp)
    