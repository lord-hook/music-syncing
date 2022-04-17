from jmespath import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


#you need to download a chrome driver and add to a known path
driver = webdriver.Chrome(r"C:\Users\User\Documents\Executables\chromedriver.exe")
driver.get("https://linkedin.com") #open linkedin

time.sleep(2)

#find and clear username and password fields 
username_field = driver.find_element_by_xpath("//input[@name='session_key']")
username_field.clear()
password_field = driver.find_element_by_xpath("//input[@name='session_password']")
password_field.clear()

#login
username_field.send_keys("toluwalase.ajijola@gmail.com") #type email
password_field.send_keys("Linkedin#101") #type password
submit = driver.find_element_by_xpath("//button[@type='submit']").click() #press submit

time.sleep(2)

file = open('industryMembers.txt','r')
member_metadata = file.readlines()

for line in member_metadata:

    line = line.split(',')
    #Search by name
    search_query = "{} AND Sheffield".format("Mayowa Ajijola") #use boolean logic to narrow the search
    search_bar = driver.find_element_by_css_selector("input[placeholder='Search']")
    search_bar.clear()
    search_bar.send_keys(search_query) #create a avriable
    search_bar.send_keys(Keys.RETURN)

    time.sleep(2)

    #CLick on message button
    all_buttons = driver.find_elements_by_tag_name("button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]
    message_buttons[0].click()

    time.sleep(2)


    #select message box and type meaasage
    paragraph_div  = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__contenteditable')]") #select message box
    paragraph_div.click()

    time.sleep(2)

    paragraphs = driver.find_elements_by_tag_name("p")
    paragraphs[-5].send_keys("Hey {0} I really appreciate the work that you've done on {1}  as a  {2}   I have been watching the series for some time, I love what you do, I'd love to pick your brain sometime and just want to let you know that your doing a great job, Thank you, It’ll be great to connect on here.".format(line[0],line[2],line[1])) #type message

    time.sleep(2)

    send_message = driver.find_element_by_xpath("//button[@type='submit']")
    send_message.click() #send message

    time.sleep(2)

    #Has to close messaging tab so the paragraphs[-5].send_keys("Hello")
    # retains it's index
    close_messenger = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
    close_messenger.click()