import time
import re
from unicodedata import name
from bs4 import BeautifulSoup
from regex import E
import requests

#read in the links for the cast and crew pages
file = open('links', 'r')
links_to_cast_and_crews = file.readlines()


try:
  #write the music department name
    for c in links_to_cast_and_crews:

        print(c)
        
        response = requests.get(c)

        soup = BeautifulSoup(response.text, 'html.parser')

        movie_title = soup.find('a', class_="subnav_heading").text#get the title of the movie

        music_department_table = soup.find('h4', id="music_department").findNext('table')


        music_department_length = 0

        #get how many members are in the music department
        for x in music_department_table.find_all('td', class_="credit"):
            music_department_length += 1


        # music_department_member_occupations = music_department_table.find_all('td', class_="credit")
        # members_occupation = music_department_member_occupations[0].text
        # members_occupation = re.sub("[\(\[].*?[\)\]]", "", members_occupation) #remove year at the end
        # members_occupation =  re.sub('[:]','', members_occupation) #remove the number at the start
        # members_occupation = members_occupation.strip()
        
        f = open('industryMembers.txt','a+')

        i = 0
        # #write music department occupation into a file
        while i < music_department_length:
            #get members name
            music_department_member_names =   music_department_table.find_all('td', class_="name")
            member = music_department_member_names[i].text
            member = member.strip()
            #get members occupation
            music_department_member_occupations = music_department_table.find_all('td', class_="credit")
            members_occupation = music_department_member_occupations[i].text
            members_occupation = re.sub("[\(\[].*?[\)\]]", "", members_occupation) #remove year at the end
            members_occupation =  re.sub('[:]','', members_occupation) #remove the number at the start
            members_occupation = members_occupation.strip() #remove leading and trailing spaces

            #print(member + "," + members_occupation)
            f.write( member + "," + members_occupation + "," + movie_title + "\n")
           
            i += 1


        # f = open('industryMembers.txt','a+')
        # for member in music_department_members:
            
        #     f = open('industryMembers.txt','a+')
        #     #f.write("\n")
except Exception as e: 
    print(e)
    # pass
    # print("no department")


    