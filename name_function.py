def get_formatted_name(first,last,middle=''):
    '''format full name 组件全名字 '''
    if middle:
        full_name=first+' '+last+' '+middle
    else:
        full_name=first+' '+last
    return full_name.title()