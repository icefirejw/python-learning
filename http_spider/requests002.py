'''
'''
import requests
import bs4

def open_url(url):
    headers = {"User-Agent":"Mozilla/5.0 (Microsoft Windows NT 10.0.17134.0; NutstoreApp-4.1.7)"}

    res = requests.get(url, headers = headers)
    return res

def get_depth(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    depth = soup.find("span", class_ = "next").previous_sibling.previous_sibling.text
    return int(depth)

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # get the movie's name
    movie_name = []
    contents = soup.find_all("div", class_ = "hd")
    for each in contents:
            movie_name.append(each.a.span.text)

    # get the movie's rate
    rate = []
    contents = soup.find_all("span", class_ = "rating_num")
    for each in contents:
        rate.append(" 评分: %s " % each.text)
    
    # get the movie's description
    desc = []
    contents = soup.find_all("div", class_ = "bd")
    for each in contents:
        try:
            desc.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    # get the movie's result
    result = []
    length = len(movie_name)
    for i in range(length):
        try:
            result.append(movie_name[i] + rate[i] + desc[i] + '\n')
        except:
            continue
    return result
     
def get_movie():
    # 打开网址，建立连接
    url_base =  "https://movie.douban.com/top250"
    res = open_url(url_base)
    
    # 获取全部的页数
    depth = get_depth(res)
    #print(depth)
    # 获取所有的电影名
    movie_names = []
    for i in range(depth):
        url = url_base + "?start=" + str(i*25) + "&filter="
        #print(url)
        res = open_url(url)
        movie_names.extend(find_movies(res))
    
    print(movie_names)
    # writing to file
    with open("movie_top250.txt", "w", encoding = "utf-8") as f:
        for each in movie_names:
            f.write(each)


if __name__ == "__main__": 
    #显示Top 250的影片名字 
    get_movie()                     

