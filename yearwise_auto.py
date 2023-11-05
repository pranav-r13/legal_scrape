#import statements
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
#from webdriver_manager.chrome import ChromeDriverManager

def details(name_tag,year):

    year_from = "01-01-"+year
    year_to = "31-12-"+year
    #setting the chromedriver to headless mode
    #driver = webdriver.Chrome('/Users/littlebuddha/Documents/Internship/Selenium-Project/chromedriver')
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver = webdriver.Chrome()
    chrome_options = Options()
    #chrome_options.add_argument("--headless")

    web = webdriver.Chrome(options=chrome_options)
    web.get('https://karnatakajudiciary.kar.nic.in/hckweb/casemenu.php')

    time.sleep(2)
    # Input of data in the necessary fields

    party_field = web.find_element("xpath",'//*[@id="parsearch-tab"]')
    party_field.click()

    time.sleep(1)

    name_field = web.find_element("xpath",'//*[@id="pt_name"]')
    name_field.send_keys(name_tag)

    fromyear_field = web.find_element("xpath",'//*[@id="ptfrom_date"]')
    fromyear_field.send_keys(year_from)

    toyear_field = web.find_element("xpath",'//*[@id="ptto_date"]')
    toyear_field.send_keys(year_to)

# captcha solver
    captcha = web.find_element("xpath",'//*[@id="captcha"]')
    src = captcha.get_attribute('https://karnatakajudiciary.kar.nic.in/hckweb/captcha.php')

    location = captcha.location
    size = captcha.size

    print(location,size)



    driver.get('https://karnatakajudiciary.kar.nic.in/hckweb/captcha.php')
    driver.save_screenshot("screenshot.png")
   
   
    #urllib.urlretrieve(src,"captcha.png")
    

    enter_cap = web.find_element("xpath",'//*[@id="vercode"]')
    enter_cap.send_keys()


    pet_res = web.find_element("xpath",'//*[@id="pt_type1"]')
    pet_res.click()

    dont_know = web.find_element("xpath",'//*[@id="pt_type1"]/option[4]')
    dont_know.click()

    get_details = web.find_element("xpath",'//*[@id="nav-tabContent"]/div[7]/div[3]/div/input')
    get_details.click()
    
    
    # # printing details 
 
    # time.sleep(2)

    # soup = BeautifulSoup(web.page_source, 'lxml')

    # tables = soup.find_all('table')
    # dfs = pd.read_html(str(tables))

    # print(f'Total tables: {len(dfs)}')
    # print(dfs[0])



# print("Enter Petitioner or respondant name : ")
name_tag = "tata"
# print("Enter the year of filing")
year = "2020"
details(name_tag,year)