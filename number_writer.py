#json文件存储数据
import json
numbers=[2,3,5,7,11,13]
fileName='File/jsonFile.json'
with open(fileName,'w') as file_object:
    json.dump(numbers,file_object)