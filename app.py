#Import statements 

from flask import Flask, render_template, request, url_for
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
from IPython.display import HTML

def details(name_tag,year):

    year_from = "01-01-"+year
    year_to = "31-12-"+year
    #setting the chromedriver to headless mode
    driver = webdriver.Chrome('/Users/littlebuddha/Documents/Internship/Selenium-Project/chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    web = webdriver.Chrome(options=chrome_options)
    web.get('http://karnatakajudiciary.kar.nic.in/search_partyname.php')

    time.sleep(2)
    # Input of data in the necessary fields

    name_field = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[3]/div[2]/div/input')
    name_field.send_keys(name_tag)

    fromyear_field = web.find_element("xpath",'//*[@id="from_date"]')
    fromyear_field.send_keys(year_from)

    toyear_field = web.find_element("xpath",'//*[@id="to_date"]')
    toyear_field.send_keys(year_to)

    get_details = web.find_element("xpath",'//*[@id="caseDetails"]/div/div/div/div[1]/div[4]/div[4]/input')
    get_details.click()
    # printing details 
 
    time.sleep(2)

    soup = BeautifulSoup(web.page_source, 'lxml')

    tables = soup.find_all('table')
    # dfs = pd.read_html(str(tables))
    # dfs = dfs.to_html()
    # print(f'Total tables: {len(dfs)}')
    # print(dfs[0])
    return tables


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        table_dets = details(name,year)
        # print(table_details)
        time.sleep(3)
        return render_template('result.html',table_dets = table_dets)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

     