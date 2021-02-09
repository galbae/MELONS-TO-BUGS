from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import ssl

context = ssl._create_unverified_context()

#urllib.request.urlretrieve(imgUrl, "test.jpg")

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options) 

#주소로이동
driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=489643191')
time.sleep(1)
#countingamount
count_xpath = "/html/body/div/div[2]/div/div/div[2]/div/h3/span"
count = driver.find_element_by_xpath(count_xpath)
amount = list(str(count.text))
x = int(amount[1] + amount[2]) #갯수


#listup
songname = []
for i in range(1,x+1):
    name_song = "/html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr["+str(i)+"]/td[3]/div/div/a[2]"
    name = driver.find_element_by_xpath(name_song)
    songname.append(name.text)
print(songname)

artistname = []
for i in range(1,x+1):
    name_artist = "/html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr["+str(i)+"]/td[4]/div/div/a"
    name = driver.find_element_by_xpath(name_artist)
    artistname.append(name.text)
print(artistname)
    
#down
import ssl
driver.get('https://music.bugs.co.kr/')
time.sleep(1)
count = 0
for i in range(len(songname)):
    count = count + 1
    elem = driver.find_element_by_id("headerSearchInput")
    elem.send_keys(songname[i]+ " " + artistname[i])
    driver.find_element_by_id("hederSearchFormButton").click()
    time.sleep(1)
    posting = driver.find_element_by_xpath('/html/body/div[2]/div[2]/article/section[2]/div/div/table/tbody/tr/td[2]/a')
    posting.click()
    time.sleep(0.5)
    posting = driver.find_element_by_xpath('/html/body/div[2]/div[2]/article/section[1]/div/div[1]/div/ul/li/a')
    posting.click()
    time.sleep(0.5)

    ssl._create_default_https_context = ssl._create_unverified_context

    imgurl = driver.find_element_by_css_selector("#originalPhotoViewBtn > img").get_attribute("src")

    urllib.request.urlretrieve(imgurl, str(count) + ".jpg")

    posting = driver.find_element_by_xpath("/html/body/div[4]/button")
    posting.click()

print('COMPLETE!')

#첫번째곡 xpath = /html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr[1]/td[3]/div/div/a[2]
#첫번째곡 아티스트 xpath = /html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr[1]/td[4]/div/div/a

#두번째곡 xpath = /html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr[2]/td[3]/div/div/a[2]
#두첫번째곡 아티스트 xpath = /html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr[2]/td[4]/div/div/a
#
#세번째곡 xpath = //*[@id="frm"]/div/table/tbody/tr[3]/td[3]/div/div/a[2]
#세번째곡 아티스트 xpath = /html/body/div/div[2]/div/div/div[2]/div/div[1]/form/div/table/tbody/tr[3]/td[4]/div/div/a