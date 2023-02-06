import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


path = r"C:\Users\Admin\anaconda3\geckodriver\geckodriver.exe"
path2 = r"C:\Users\Admin\anaconda3\chromedriver_win32\chromedriver.exe"
# create webdriver object

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver2 = webdriver.Chrome(executable_path=path2, options=options)


# login to twitter
driver2.get("https://twitter.com/login")
sleep(10)
# find input box to enter username
text_box = driver2.find_element(By.XPATH, "//input[@name ='text']")
text_box.send_keys('WilliamMunguti1')
sleep(2)
# find next button
Next = driver2.find_element(By.XPATH, "//span[contains(text(),'Next')]")
Next.click()
sleep(3)

# find input to enter password
password = driver2.find_element(By.XPATH, "//input[@name ='password']")
password.send_keys('muntuiwilliam97@gmail.com0724551906')
sleep(3)

# find login button
Login = driver2.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
sleep(2)
Login.click()

# profile to search on Twitter
profile = 'Qhala HQ'

# find search input
sleep(10)
search = driver2.find_element(By.XPATH, "//input[@type='text']")
# enter profile to search
search.send_keys(profile)
sleep(2)
# press enter on the keyboard
search.send_keys(Keys.ENTER)
sleep(3)

# find people section on Twitter page
people = driver2.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()
sleep(12)

#find element containing profile
prof = driver2.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span")
prof.click()
sleep(2)
# lists to store and hold variables temporarily while appending them
TimeStamps = []
User_tags = []
Retweets = []
Tweets = []
Replys = []
Likes = []


try:
    attempts = 1
    # get all tweets in the profile
    articles = driver2.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    sleep(3)
    while True:
        for article in articles:
            sleep(0.1)
            Tweets2 = list(set(Tweets))
            User_tag = driver2.find_element(By.XPATH, ".//div[@data-testid='User-Names']").text
            User_tags.append(User_tag)

            Time_stamp = driver2.find_element(By.XPATH, ".//time").get_attribute('datetime')
            TimeStamps.append(Time_stamp)

            Tweet = driver2.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
            Tweets.append(Tweet)

            Reply = driver2.find_element(By.XPATH, ".//div[@data-testid='reply']").text
            Replys.append(Reply)

            Retweet = driver2.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
            Retweets.append(Retweet)

            Like = driver2.find_element(By.XPATH, ".//div[@data-testid='like']").text
            Likes.append(Like)
            print('Twitter data is being scrapped, be patient this may take a while')
            print(len(Tweets))

        driver2.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # get another article
        articles = driver2.find_elements(By.XPATH, "//article[@data-testid='tweet']")

        # Tweets2 is another variable used to store only the unique tweets obtained from the scrape
        if len(Tweets) >= 800:
            print(len(Tweets))
            break
    df = pd.DataFrame(zip(User_tags, TimeStamps, Tweets, Replys, Retweets, Likes), columns=['User_tags', 'TimeStamps', 'Tweets', 'Replys', 'Retweets', 'Likes'])
    # store in a csv file
    df.to_csv(r"C:\Users\Admin\Documents\Main Desktop\twitter scrapping\tweets_twitter.csv", index=False)
    print(f'{len(Tweets)} Tweets have been scrapped from profile')
    print('CSV has been Stored')
    driver2.close()
    exit()
except Exception as e:
    print(attempts)
    while True:
        attempts += 1
        if attempts == 10:
            print('The number of attempts has exceeded the limit')
            print(attempts)
            print(e)
            driver2.close()
            break
        print(attempts)
        print(e)
        continue


