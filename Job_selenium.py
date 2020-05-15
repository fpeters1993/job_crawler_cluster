import urllib
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os
import re

#/usr/lib/chromium-browser/

# establish Selenium
# ToDo in new function
driver = webdriver.Firefox(executable_path='/home/finn/Downloads/geckodriver')
driver.get('https://www.service.bund.de/Content/DE/Stellen/Suche/Formular.html?nn=4642046&type=0&submit=Finden&cl2Categories_Laufbahn=laufbahn-gehobenerdienst&city_zipcode=Hamburg')

# get content
# ToDo in new function
page = driver.page_source
job_soup = BeautifulSoup(page, "html.parser")

# get job-list
liste = job_soup.find('ul', class_='result-list')

# todo check if already done
def get_content():
    driver = webdriver.Firefox(executable_path='/home/finn/Downloads/geckodriver')
    driver.get('https://www.service.bund.de/Content/DE/Stellen/Suche/Formular.html?nn=4642046&type=0&submit=Finden&cl2Categories_Laufbahn=laufbahn-gehobenerdienst&city_zipcode=Hamburg')
    page = driver.page_source
    job_soup = BeautifulSoup(page, "html.parser")
    liste = job_soup.find('ul', class_='result-list')
    return liste

# todo check if extraction is working
def extract_information():
    job_df = pd.DataFrame(columns=['link', 'titel', 'Text'])
    counter = 0
    get_content()
    driver = webdriver.Firefox(executable_path='/home/finn/Downloads/geckodriver')
    liste_detail = liste.find_all('a')
    for link in liste_detail:
        link_new = 'https://www.service.bund.de/' + link['href']
        title = link['title'].replace('Zur Detailseite', '')
        job_df.loc[counter, 'link' ] = link_new
        job_df.loc[counter, 'titel'] = title
        driver.get(link_new)
        page = driver.page_source
        job_soup = BeautifulSoup(page, "html.parser")
        detail = job_soup.find_all('section')
        job_df.loc[counter, 'Text'] = detail[4]
        counter +=1
    return job_df

# todo main function?
df = extract_information()




# todo modularize
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# remove 
df['Text'].apply(pd.Series).stack().replace('\n', '').dr


for i in df.index:
    df.iloc[i]['Text'] = remove_html_tags(df.iloc[i]['Text'])

df['Text']





