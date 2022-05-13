from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#===================

HOME_PAGE = "https://vb.knowledgematters.com/"

READING_QUIZ_URL = "https://vbcourse.knowledgematters.com/quiz/answerQuestion/2839{0}/2391407/{1}" 
READING_QUIZ_ARGS = [("851", "1"), ("853", "3"), ("11823", "2"), ("11825", "0"), ("11394", "1"), ("857", "2"), ("860", "1"), ("11827", "1"), ("956", "2"), ("11828", "1")] 


MATH_QUIZ_URL = "https://vbcourse.knowledgematters.com/quiz/answerQuestion/2839{0}/2391408/{1}" 
MATH_QUIZ_ARGS = [("601", "3"), ("11398", "3"), ("11397", "1"), ("11393", "0"), ("11394", "2"), ("11390", "2"), ("602", "1"), ("11395", "1"), ("605", "0"), ("603", "1")] 

#======== [IMPORTANT] Select the parameters you want

QUIZ_URL = READING_QUIZ_URL
QUIZ_ARGS = READING_QUIZ_ARGS

#===================

def login(driver):
    driver.get(HOME_PAGE)
    driver.find_element_by_name("email").send_keys("[USERNAME]")
    driver.find_element_by_name("password").send_keys("[PASSWORD]")
    driver.find_element_by_id("login_button").send_keys(Keys.ENTER)

driver = webdriver.Chrome()

login(driver)


for quizID in range(881, 901):
    print("Quiz: #{0}".format(quizID + 1))
    for question in range(0, 10): #Start from 0 when not testing
        print("Question: #{0}".format(question + 1))
        driver.get(QUIZ_URL.format(quizID, QUIZ_ARGS[question][0]))
        driver.find_element_by_xpath("//td[@style='vertical-align:top; padding-top:0px;']//input[@aria-labelledby='rad{0}a rad{0}b']".format(QUIZ_ARGS[question][1])).click()
        #input() #for testing
        driver.find_element_by_id("submitBtn").send_keys(Keys.ENTER)
    driver.get(QUIZ_URL.format(quizID, ""))
        







        





