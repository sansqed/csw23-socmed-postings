import requests
import random

from mySecrets import username, password

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd
import json
import random

class FaceBookBot():

    def __init__(self):

        # INITIALIZE SELENIUM WEBDRIVER
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        # READ AN INITIALIZE DATAFRAME
        # fields = ['id', 'author', 'author_img', 'date_time', 'text', 'imgs']
        # self.df = pd.read_json("../src/posts.json")
        # print(self.df)

    def randomScroll(self):
        direction = random.randrange(0,10)
        for i in range(random.randrange(100,1000)):
            if direction%2 ==0:
                rate = "window.scrollBy(0,"+ str(random.randrange(1,6)) +")"
                self.driver.execute_script(rate)
            else:
                self.driver.execute_script("window.scrollBy(0,-1)")


    def login(self):
        print("LOGGING IN TO FACEBOOK")
        
        # LOGIN TO FACEBOOK
        self.driver.get("https://mbasic.facebook.com/login.php")

        # ENTER USERNAME
        email_in = self.driver.find_element(By.NAME, 'email')
        # email_in.send_keys(username)
        self.sendKeysSlow(email_in, username)

        # ENTER PASSWORD
        pass_in = self.driver.find_element(By.NAME, 'pass')
        # pass_in.send_keys(password)
        self.sendKeysSlow(pass_in, password)

        sleep(1)
        # PRESS LOGIN BUTTON
        login_btn = self.driver.find_element(By.NAME, 'login')
        login_btn.click()

        # sleep(WAIT_TIME)
        sleep(1)
        # PRESS NOT NOW WHEN PROMPTED WITH ONE-TAP LOGIN OPTION
        notnow_btn = self.driver.find_element(By.CLASS_NAME, "bo")
        notnow_btn.click()
        print("LOGGED IN")
    def sendKeysSlow(self, s, txt):
        for t in txt:
            s.send_keys(t)
            sleep(0.3)

    def scrapeFBPosts(self, hashtag):

        # uses mobile version instead of mbasic bec more posts are loaded   
        print("SCRAPING #"+hashtag)
        self.driver.get("https://mobile.facebook.com/hashtag/"+hashtag) # Navigate to hashtag link

        sleep(WAIT_TIME) # Waits for loading time of posts

        soup = BeautifulSoup(self.driver.page_source,"html.parser") # initialize beautifulsoup

        stories = soup.find_all("div", "story_body_container") # scrapes all posts relating to hashtag

        # print(stories)
        for story in stories:
            header = story.find("header", recursive=False)

            for i in range(random.randrange(2,5)):
                self.randomScroll()

            thisPost = {
                "id":"",
                "author": "",
                "date_time": "", 
                "author_img": "",
                "text": "",
                "imgs": "",
                "src": "Facebook",
            }

            if header: # sometimes header is nonexistent
                iddiv = story.parent["data-ft"]
                
                id = iddiv[22:iddiv.find('"', 22)]
                
                # print(id in self.df['id'].values.astype(str))
                try:
                    idx =  self.df.id[self.df.id.astype(str) == id].index[0]
                except:
                    idx = -1
                if idx != -1:
                    print("  POST ALREADY IN DATAFRAME")
                    self.df["date_time"][idx] = str(header.find("abbr").text)
                    continue
                
                thisPost["id"] = iddiv[22:iddiv.find('"', 22)] # gets post id stored in data-ft attribute of div

                thisPost["author"] = header.find("strong").text # gets author of post
        
                thisPost["date_time"] = header.find("abbr").text # get date time of post

                # GET PROFILE PIC OF AUTHOR
                temp = header.find("i")["style"]
                start = temp.find('(')+2
                end = temp.find(')')-1
                thisPost["author_img"] = self.convertSaltedLink(temp[start:end])

                # GET TEXTS
                textdiv = header.find_next_sibling("div")
                text = textdiv.find("span")
                text["class"] = "text_exposed" # forces the post to expand, similar to pressing "see more..."
                text = text.text
                thisPost["text"] = text

                # GET IMAGES
                imgsdiv = textdiv.find_next_sibling("div")
                if imgsdiv:
                    imgs = imgsdiv.select("div > div > div > a") + imgsdiv.select("section > div")
                    for img in imgs:
                        iarr = img.select("div > i")
                        for i in iarr:
                            style = i["style"]
                            start = style.find('(')+2
                            end = style.find(')')-1
                            link = self.convertSaltedLink(style[start:end]) # replace salted link by fb
                            thisPost["imgs"] += link + ' '

                print("New post")

                thisPost = pd.DataFrame([thisPost])
                print(thisPost)

                # APPEND TO DATAFRAME
                self.df = pd.concat([thisPost, self.df], ignore_index = True)
                self.df.reset_index()

        print("EXPORTING TO JSON")
        self.df.to_json("../src/posts.json", orient="records")
        print("DONE SCRAPING")

    def convertSaltedLink(self, link):
        # SINCE SPECIAL CHAR IN LINKS OF IMAGES ARE SALTED
        # '\\' ESCAPE CHARACTER TO RECOGNIZE FORWARD SLASH 
        return link.replace('\\3a ', ':').replace('\\3d ', '=').replace('\\26 ','&')
def runBot():
    bot = FaceBookBot()
    bot.login()

    # SET CONFIG VALUES
    config = json.load(open("../src/config.json","r"))

    HASHTAGS = config["HASHTAGS"]
    WAIT_TIME = config["WAIT_TIME"] # in seconds
    LOOP_DELAY = config["LOOP_DELAY"] # in seconds

    # SCRAPES ALL HASHTAGS
    # WAITS FOR LOOP DELAY
    while 1:
        bot.scrapeFBPosts(HASHTAGS[random.randrange(0, len(HASHTAGS))])
        sleep(random.randrange(LOOP_DELAY/2, LOOP_DELAY))
        print("LOOP DELAY\n")
        sleep(random.randrange(LOOP_DELAY/2, LOOP_DELAY))

bot = FaceBookBot()
for i in range(10):
    bot.randomScroll()
sleep(50)