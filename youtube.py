import time

import pandas as pd

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import json

driver = webdriver.Chrome()

url = 'https://www.youtube/examplechannel/video/'#You have to upload URl of the videos page for scraping

driver.get(url)

driver.maximize_window()

for i in range(0,31):   #loop to scroll down till the last video you can change the from 31 to any other according to your need.
    
    last.send_keys(Keys.END)
    
    time.sleep(3)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer') #finding all the videos present in the page.

count = 1

data = {'Title' : [],         #creating a dictionary for storing scrape data.
       'Link' : [],
        'Views' : [],
        'Upload on' : [],
        'Channel' : [],
        'Channel link' : []
       }

channel_link = 'https://www.youtube/examplechannel/'

channel = 'Channel name'

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
    
    data_frame.to_excel('file.xlsx')
        
    print(f'{count} :- title = {title}\n\tviews = {views}\n\tupload on {upload_date}\n\tlink = {links[0]}\n\tchannel = {channel}\n\tchannel link = {channel_link}')
        
    count += 1"""
