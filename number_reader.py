
#读取json 文件数据
import json
fileName='File/jsonFile.json'
with open(fileName) as file_object:
    numbers=json.load(file_object)
    print(numbers)