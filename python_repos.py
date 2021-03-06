import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行api调用并存储响应
try:
    url="https://api.github.com/search/repositories?q=language:python&sort=stars"
    r=requests.get(url)
    print("Status code:",r.status_code)
    #将API响应存储在一个变量中
    response_dict=r.json()
    print("Total repositories:",response_dict['total_count'])
    #探索有关仓库的信息
    repo_dicts=response_dict['items']
    #print("Repositories returned:",len(repo_dicts))
    names,starts=[],[]
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        starts.append(repo_dict['stargazers_count'])
    #可视化
    my_style=LS('#333366',base_style=LCS)
    my_config=pygal.Config()
    my_config.x_label_rotation=45
    my_config.show_legend=False
    my_config.title_font_size=24
    my_config.lable_font_size=14
    my_config.major_lable_font_size=18
    my_config.truncate_lable=15
    my_config.show_y_guides=False
    my_config.width=1000

    chart=pygal.Bar(my_config,style= my_style)
    chart.title='Most-starred Python Projects on GitHub'
    chart.x_labels=names
    chart.add('',starts)
    chart.render_to_file('python_repos.svg')

    """
    #研究第一个仓库
    repo_dict=repo_dicts[0]
    print("\nkeys:",len(repo_dict))
    for key in sorted(repo_dict.keys()):
        print(key)
    """

    """
    #研究有关仓库的信息
    print("\n Selected information about each repository: ")
    for repo_dict in repo_dicts:
        print('\nName:',repo_dict['name'])
        print('Owner:', repo_dict['owner']['login'])
        print('Starts:', repo_dict['stargazers_count'])
        print('Repository:', repo_dict['html_url'])
        print('Description:', repo_dict['description'])
    """
    """
    #结果写入文件
    fileName='File/RepositoriesOfPython.txt'
    with open(fileName,'w',encoding='utf-8') as file_object:
        for repo_dict in repo_dicts:
            file_object.write('\n\nName: '+repo_dict['name'])
            file_object.write('\nOwner: '+repo_dict['owner']['login'])
            file_object.write('\nStarts: '+str(repo_dict['stargazers_count']))
            file_object.write('\nRepository: '+repo_dict['html_url'])
            file_object.write('\nDescription: '+str(repo_dict['description']))
    """

except ConnectionResetError:
    print("连接错误！")

