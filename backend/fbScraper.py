from secrets import email, password
import requests

from bs4 import BeautifulSoup

payload = {
    'email': "asdfasdf@aqumail.com",
    'encpass': "#PWD_BROWSER:5:1679077969:AZ9QAK+hM0KFePSu87gBFwqaTerOrO9iD5Oz0RMnViv6FEgrpSgu3q81fdM5L5zOX31wZnpZbCPG77TvJhOhR+gOPVQ4c0Ddu0MxHUHWKqAv1drqdfu9HsZecNDsIXLUDmm8ateZDb4tghUYqi+kwSLVfc4V1vmdAiLC",
}

# LOGIN_URL = "https://mbasic.facebook.com/login.php?"

# with requests.Session() as session:
#     post = session.post(LOGIN_URL, data=payload)
#     # print(post)
#     page = requests.get("https://web.facebook.com/hashtag/komsaiweek2023?refsrc=deprecated&_rdc=1&_rdr")
#     soup = BeautifulSoup(page.content, "html.parser")
#     # print(soup)
#     test = soup.find_all('div')
#     print(test)
#     # print("testing")
#     # for i in test:
#     #     print(i.text)

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

page = requests.get(url="https://web.facebook.com/hashtag/komsaiweek2023", headers=headers)
print(page.text)
# soup = BeautifulSoup(page.content, "html.parser")
# test = soup.find_all('div')
# print(test)