#有序字典
from collections import OrderedDict
favorite_languages=OrderedDict()
favorite_languages['jens']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+'.' )

fav_languages={'jens':'python','sarah':'c','edward':'ruby','phil':'python'}
for name,lan in fav_languages.items():
    print(name.title()+"'s favorite language is "+lan.title()+'.' )