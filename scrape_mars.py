from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime
import pymongo
from pymongo import MongoClient

def instantiate_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=r'C:\Users\chutc\Documents\Class Work\chromedriver.exe', 
        chrome_options=chrome_options)
    return driver

driver = instantiate_driver()

news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

driver.get(news_url)

news_title = driver.find_element_by_class_name("content_title").text
print(news_title)

news_p = driver.find_element_by_class_name("article_teaser_body").text
print(news_p)

news_dict = {}
news_dict['title'] = news_title
news_dict['teaser'] = news_p

image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

driver.get(image_url)

full_image = driver.find_element_by_xpath('//*[@id="full_image"]')

relative_link = full_image.get_attribute('data-fancybox-href')
featured_image_url = 'https://www.jpl.nasa.gov' + str(relative_link)
print(featured_image_url)

mars_weather_url = "https://twitter.com/marswxreport?lang=en"

driver.get(mars_weather_url)

tweets = driver.find_elements_by_class_name("js-tweet-text-container")

[x.text for x in tweets]

tweets[10].text

mars_weather = tweets[10].text
print(mars_weather)

cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"

driver = instantiate_driver()
driver.get(cerberus_url)

ceb_xpath = driver.find_element_by_xpath('//*[@id="wide-image"]/img')

ceb_img_url = ceb_xpath.get_attribute('src')
print(ceb_img_url)

ceb_title = driver.find_element_by_css_selector('h2').text
print(ceb_title)

ceb_dict = {}
ceb_dict['img_url'] = ceb_img_url
ceb_dict['title'] = ceb_title

schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

driver.get(schiaparelli_url)

schia_xpath = driver.find_element_by_xpath('//*[@id="wide-image"]/img')

schia_img_url = schia_xpath.get_attribute('src')
print(schia_img_url)

schia_title = driver.find_element_by_css_selector('h2').text
print(schia_title)

schia_dict = {}
schia_dict['img_url'] = schia_img_url
schia_dict['title'] = schia_title

syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

driver.get(syrtis_url)

syrtis_xpath = driver.find_element_by_xpath('//*[@id="wide-image"]/img')

syrtis_img_url = syrtis_xpath.get_attribute('src')
print(syrtis_img_url)

syrtis_title = driver.find_element_by_css_selector('h2').text
print(syrtis_title)

syrtis_dict = {}
syrtis_dict['img_url'] = syrtis_img_url
syrtis_dict['title'] = syrtis_title

valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

driver.get(valles_url)

valles_xpath = driver.find_element_by_xpath('//*[@id="wide-image"]/img')

valles_img_url = valles_xpath.get_attribute('src')
print(valles_img_url)

valles_title = driver.find_element_by_css_selector('h2').text
print(valles_title)

valles_dict = {}
valles_dict['img_url'] = valles_img_url
valles_dict['title'] = valles_title

hemisphere_image_urls = [ceb_dict, schia_dict, syrtis_dict, valles_dict]

def scraped():
    all_data = {}
    all_data['hemisphere_image_urls'] = hemisphere_image_urls
    all_data['mars_news'] = news_dict
    all_data['feat_img'] = featured_image_url
    all_data['mars_weather'] = mars_weather
    return all_data