from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time
import re
from bs4 import BeautifulSoup
import requests



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\User\Documents\Executables\chromedriver.exe")
#you need to download a chrome driver and add to a known path
#river = webdriver.Chrome(r"C:\Users\User\Documents\Executables\chromedriver.exe")

#initial_movie_page = "https://www.imdb.com/search/title/?genres=crime&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f1cf7b98-03fb-4a83-95f3-d833fdba0471&pf_rd_r=XPGX4BEP6E8VKJSN885S&pf_rd_s=center-3&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr3_i_3"
initial_movie_page = "https://www.imdb.com/search/title/?genres=crime&start=701&explore=title_type,genres&ref_=adv_nxt"
#start from a direct link to each genre pg 
driver.get(initial_movie_page) #open imdb crime pg

time.sleep(2)

#select genre
#Grab a pg worth of movies
#block_of_movies = driver.find_elements(by=By.CLASS_NAME, value='lister-item')

next_page_of_movies = ""

i = 0
while_loop_iteration_count = 1

f = open('crimeCastAndCrewPages.txt','a+')
#Set up for loop to run through all the movies on that pg
while i < 50:
    print(i)
    #first iteration already grabs this element
    block_of_movies = driver.find_elements(by=By.CLASS_NAME, value='lister-item')

    #Extracting movie title
    try:
        movie_title = block_of_movies[i].find_element(by=By.CLASS_NAME, value='lister-item-header').text
    except:
        continue

    movie_title = re.sub("[\(\[].*?[\)\]]", "", movie_title) #remove year at the end
    movie_title = movie_title[movie_title.find('.'):]
    #movie_title =  re.sub('[0123456789]','', movie_title) #remove the number at the start
    movie_title = movie_title[1:] #remove the . at the start
    movie_title = movie_title.strip() #remove leading and trailing spaces
    

    #extract link to movie
    movie_link = driver.find_element(by=By.LINK_TEXT, value=movie_title) #find movie link
    movie_link.click()


    #go to the cast and crew page
    full_cast_crew = driver.find_element(by=By.XPATH, value="//a[starts-with(@class, 'ipc-metadata-list-item__label')]")
    full_cast_crew.click()

    time.sleep(2)

    #file to write the cast and crew links
    f.write(driver.current_url)
    f.write("\n")

    time.sleep(2)

    #go back to the first list of movies 
    if  while_loop_iteration_count == 1:
        driver.get(initial_movie_page)

    #go to the pg with the list of moview
    elif while_loop_iteration_count > 1:
         driver.get(next_page_of_movies)

    time.sleep(2)


    #reset the while loop and move to the next page of movies
    if i == 49: 
        #need to test for and go to the new page
        i=0
        while_loop_iteration_count += 1

        next_page = driver.find_element(by=By.LINK_TEXT, value="Next »")
        next_page.click()

        time.sleep(3)

        next_page_of_movies = driver.current_url

    else:
        i += 1




