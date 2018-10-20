import urllib.request

def get_content(s):
    url = s
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.info())
    print(response.getcode())

def translation(s):
    req = urllib.request.Request();


if __name__ == "__main__":
    get_content("http://placekitten.com/200/300")

