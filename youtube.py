import time

import pandas as pd

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import json

driver = webdriver.Chrome()

url = 'https://www.youtube.com/c/HBAServices/videos'

driver.get(url)

driver.maximize_window()

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    print (lenOfPage)
    if lastCount==lenOfPage:
        match=True

"""videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

count = 1

data = {'Title' : [],
       'Link' : [],
        'Views' : [],
        'Upload on' : [],
        'Channel' : [],
        'Channel link' : []
       }

channel_link = 'https://www.youtube.com/c/HBAServices/'

channel = 'John Watson Rooney'

for video in videos:

    video_link = video.find_elements_by_xpath('.//*[@id="thumbnail"]')
    
    links = list(dict.fromkeys(map(lambda a : a.get_attribute('href'),video_link)))
    
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    
    upload_date = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    
    data['Title'].append(title)
    
    data['Link'].append(links[0])
    
    data['Views'].append(views)
    
    data['Upload on'].append(upload_date)
    
    data['Channel'].append(channel)
    
    data['Channel link'].append(channel_link)
    
    data_frame = pd.DataFrame(data)
    
    data_frame.to_excel('hba_channel.xlsx')
        
    print(f'{count} :- title = {title}\n\tviews = {views}\n\tupload on {upload_date}\n\tlink = {links[0]}\n\tchannel = {channel}\n\tchannel link = {channel_link}')
        
    count += 1"""