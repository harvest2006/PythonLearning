import json
#将数据加载到一个列表
filename="btc_close_2017.json"
with open(filename) as f:
    btc_data=json.load(f)
"""
#打印每一天的信息
for btc_dict in btc_data:
    date=btc_dict['date']
    month =int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close =int(float(btc_dict['close']))
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date,month, week, weekday, close))
"""
dates, months, weeks, weekdays, closes = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))
import pygal

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价折线图(￥).svg')