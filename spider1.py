# 观察者模式
import re
import requests
from bs4 import BeautifulSoup

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
        pattern1 = re.compile('<a.*?href="(.*?)".*?>.*?</a>')
        a = re.findall(pattern1, self.content)
        return a

    # 返回解析出来的文本
    def getTitle(self, url):
        self.response = requests.get(url)
        self.content = self.response.text
        pattern2 = re.compile('<a.*?html.*?>(.*?)</a>')
        b = re.findall(pattern2, self.content)
        return b

    def getText(self, url):
        artical = []
        self.response = requests.get(url)
        self.response.encoding = 'utf-8'
        soup = BeautifulSoup(self.response.text, 'html.parser')
        article2 = soup.select('p')
        for p in article2:
            artical.append(p.text.strip())
        return artical

# 主方法
if __name__ == '__main__':
    sub = Subjects()
    url = sub.getUrl("https://voice.hupu.com/nba/2529865.html")
    title = sub.getTitle("https://voice.hupu.com/nba/2529865.html")
    text = sub.getText("https://voice.hupu.com/nba/2529865.html")
    # 将得到的新闻url保存在url.txt文件中
    f1 = open("url.txt", "w")
    for i in url:
        f1.write(i)
        f1.write("\n")
    f1.close()

    # 将得到的新闻标题保存在title.txt文件中
    f2 = open("title.txt", "w")
    for j in title:
        f2.write(j)
        f2.write("\n")
    f2.close()

    # 将得到的新闻内容保存在text.txt文件中
    f3 = open("text.txt", "w", encoding='utf-8')
    for k in text:
        f3.write(k)
        f3.write("\n")
    f3.close()

    # https://voice.hupu.com/nba
    # https://voice.hupu.com/nba/2529865.html