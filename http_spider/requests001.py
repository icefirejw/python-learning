'''
using requests module
'''
import requests
import bs4

res = requests.get("https://movie.douban.com/top250")
contents = bs4.BeautifulSoup(res.text, "html.parser")
targets = contents.find_all("div", class_="hd")
for each in targets:
    print(each.a.span.text)