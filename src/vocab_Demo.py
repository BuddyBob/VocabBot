import os
import time
import random
import config
from bs4 import BeautifulSoup
from selenium import webdriver
from unidecode import unidecode
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


# Link to  assignment [For Demo]
#url = "https://www.vocabulary.com/lists/23380/practice"
# url = "https://www.vocabulary.com/lists/7701690/practice"
url = "https://www.vocabulary.com/lists/194479/practice"
#url = "https://www.vocabulary.com/lists/52473/practice"

#variables
global t
t = 0
choice = []
count = 0
#On mac it would look something like this - /Users/Myname/Downloads/chromedriver
#On windows it would look something like this - C:\Users\Myname\Downloads\chromedriver
driver = webdriver.Chrome(executable_path=config.path_to_chromedriver)
waitshort = WebDriverWait(driver,.5)
wait = WebDriverWait(driver, 20)
waitLonger = WebDriverWait(driver, 100)
visible = EC.visibility_of_element_located
login_page = "https://www.vocabulary.com/login/"
print("[+] STARTING VOCABULARY BOT")


#run program
def main():
    login()
    assignment()



#login with username info
def login():
    driver.get(login_page)
    google = wait.until(visible((By.XPATH,'//*[@id="loginform"]/div[1]/div[1]/a'))).click()
    email = wait.until(visible((By.XPATH,'//*[@id="identifierId"]'))).send_keys(config.EMAIL,Keys.ENTER)
    pwd = wait.until(visible((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(config.PASSWORD,Keys.ENTER)



#get assignment
def assignment():
    time.sleep(3)
    driver.get(url)
    option_high_score = scrapper()
    click_op(option_high_score)
    print("[+] STARTING VOCABULARY BOT")
    print("\a\a\a\a\a\a\a")



#check for correct answer
def scrapper():
    time.sleep(3)
    #get code for page
    source = unidecode(driver.page_source)
    soup = BeautifulSoup(source, "html.parser")
    length_check = len(
        soup.findAll('div', attrs={'class': 'questionContent'})[0].text.split(" "))
    if(length_check == 1):
        word = soup.findAll('strong')[-1].text
        print('word:',word)

        dic_exceptions = ['up', 'as', 'if', 'the', 'who', 'has', 'a', 'an', 'to', 'for', 'from', 'is', 'where', 'when', 'why',
                            'how', 'which', 'of', 'one', "one's", 'or', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

                        #================================  get possible answers ==========================#
        op1 = (soup.findAll('a', attrs={'accesskey': '1A'})[
                -1].text + "\n").rstrip('\n').split(" ")
        
        op2 = (soup.findAll('a', attrs={'accesskey': '2B'})[
                -1].text + "\n").rstrip('\n').split(" ")
        op3 = (soup.findAll('a', attrs={'accesskey': '3C'})[
                -1].text + "\n").rstrip('\n').split(" ")
        op4 = (soup.findAll('a', attrs={'accesskey': '4D'})[
                -1].text + "\n").rstrip('\n').split(" ")
        final = []
        options = [op1, op2, op3, op4]
                        #================================  Take out unessasary letters from Options ==========================#
        for option in options:
            for item in option:
                for x in dic_exceptions:
                    if x == item:
                        p = option.index(x)
                        option.pop(p)
        print('answers:',options)
                #================================  Rate options based on how many words in answer match words in dict ==========================#
        s_link = "https://www.vocabulary.com/dictionary/"
        link = s_link + word
        html = urlopen(link)
        soup = BeautifulSoup(html, "html.parser")
        a = 0
        source_dic = unidecode(soup.prettify())
        
        rate_arr = []
        for option in options:
            for item in option:
                if item in source_dic:
                    soup.findAll(item)
                    a += 1

            rate_arr.append(a)
            a = 0
                #================================  Option Rating ==========================#
        print(f'Occurances in dic: {rate_arr}') 
        _1OpGuess = rate_arr[0]
        _2OpGuess = rate_arr[1]
        _3OpGuess = rate_arr[2]
        _4OpGuess = rate_arr[3]
        #Return which answer to click. If there are no words that matched in the dict it will by default return 2
        if _1OpGuess > _2OpGuess and _1OpGuess >_3OpGuess and _1OpGuess >_4OpGuess: return 1
        elif _2OpGuess > _1OpGuess and _2OpGuess > _3OpGuess and _2OpGuess > _4OpGuess: return 2
        elif _3OpGuess > _1OpGuess and _3OpGuess > _2OpGuess and _3OpGuess > _4OpGuess: return 3
        elif _4OpGuess > _1OpGuess and _4OpGuess > _2OpGuess and _4OpGuess > _3OpGuess: return 4
        else:return 2

            

    else:
        driver.quit()
        exit()

    # except IndexError as e:
    #     print(e)
    #     driver.quit()
    #     main()


def click_op(i):
    #click the answer
    choice = []
    choice.append(i)
    op = i
    high = str(op)
    time.sleep(.5)
    #scan current question level
    try:
        element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
    except:
        try:
            element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[2]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
        except:
            try:
                element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[3]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
            except:
                try:
                    element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[4]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                except:
                    try: 
                        element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[5]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                    except:
                        try:
                            element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[6]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                        except:
                            try:
                                element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[7]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                            except:
                                try:
                                    element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[8]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                                except:
                                    try:
                                        element = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[9]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                                    except:
                                        try:
                                            element =driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[10]/div/div/section[1]/div[1]/div[4]/a['+high+']').click()
                                        except:
                                            try:
                                                txt = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div/div/div/section[1]/div[1]/div[1]/div[2]/strong[1]').txt
                                            except:
                                                try:
                                                    for i in range(1,10):
                                                        txt = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div['+str(i)+']/div/div/section[1]/div[1]/div[1]/div[2]/strong[1]').txt
                                                except:
                                                    driver.quit()
                                                    exit()

                                            


    try:  
        nextQ = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[2]/button').click()
    except:
        #if the previous answer was wrong choose random one
        while True:
            num = random.randint(1,4)
            if num not in choice:
                break
        click_op(num)
    
    #look for the next question
    option_high_score = scrapper()
    time.sleep(1)
    click_op(option_high_score)


#====================================================================================================================================================#
main()