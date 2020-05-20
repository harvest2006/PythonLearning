#文件操作
#with open('File/1.txt') as file_object:
    #contents=file_object.read()
    #print(contents.strip())

#with open('File/1.txt') as file_object:
    #lines=file_object.readlines()
    #for line in lines:
    #    print(line.rstrip())
'''
fileName='File/1.txt'
with open(fileName) as file_object:
    lines=file_object.readlines()
    str = ''
    for line in lines:
        str+=line.rstrip()
    print(str)
    print(len(str))
'''
'''
fileName='File/2.txt'
with open(fileName,'w') as file_object:
    file_object.write("I also love finding m.\n")
    file_object.write("I also love finding f.\n")
'''
'''
fileName='File/2.txt'
with open(fileName,'a') as file_object:
    file_object.write("I also love finding n.\n")
    file_object.write("I also love finding g.\n")
'''
fileName='File/3.txt'
try:
    with open(fileName) as file_object:
        contents=file_object.read()
        print(contents)
except FileNotFoundError:
    msg="Sorry,the file "+fileName+"dons not exist."
    print(msg)

