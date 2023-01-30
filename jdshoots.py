import requests
import json
import openpyxl
# 创建excel表格
wk = openpyxl.Workbook()
# 创建sheet
sheet = wk.create_sheet()
# 设置headers是为了解决服务器反爬机制
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8452201&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
resp = requests.get(url, headers=headers)
context = resp.text
print(context)
result = context.replace("fetchJSON_comment98(", "").replace(");", "")
json_data = json.loads(result)
# print(json_data)
comments = json_data['comments']
for item in comments:
    color = item['productColor']
    size = item['productSize']
    # 在sheet中保存数据
    sheet.append([color, size])
    # 把表格保存在一个磁盘里面 使用相对路径
    wk.save('data.xlsx')
print('数据保存成功')
