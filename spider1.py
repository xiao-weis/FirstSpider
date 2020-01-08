# 观察者模式

import re
import requests

class Subjects():
    # 初始化
    def __init__(self):
        self.response = ""
        self.content = ""
        self.url = ""

    # 返回解析出来的url
    def getUrl(self, url):
        self.response = requests.get(url)
        self.content = self.response.text
        pattern1 = re.compile('<a(.*?html).*?blank">.*?</a>')
        a = re.findall(pattern1, self.content)
        return a

    # 返回解析出来的文本
    def getText(self, url):
        self.response = requests.get(url)
        self.content = self.response.text
        pattern2 = re.compile('<p>(.*?)</p>')
        b = re.findall(pattern2, self.content)
        return b

# 主方法
if __name__ == '__main__':
    sub = Subjects()
    url = sub.getUrl("https://https://voice.hupu.com/nba")
    text = sub.getText("https://https://voice.hupu.com/nba")
    for i in url:
        print(i)
    for i in text:
        print(i)