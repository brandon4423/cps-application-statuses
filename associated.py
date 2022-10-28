import creds
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login = gspread.service_account(filename="service_account.json")
sheet_name = login.open("HOA")
worksheet = sheet_name.worksheet("CPSREF")
values = worksheet.get_values("A1:B7617")
spaddress = worksheet.get_values("B1:B7617")

# Google spreadsheets api
# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument('--ignore-certificate-errors')

# headless doesn't work with CPS portal
# options.add_argument('--headless')

browser = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=browser)
project = f"/files"
username = creds.username
password = creds.password
url = "https://secure.cpsenergy.com/welcome/solarlogin.jsp"


def scraperall():
    start_time = time.time()
    try:
        main = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.ID, 'myTable'))
        )
        tables = driver.find_elements(By.XPATH, '//*[@id="myTable"]/tbody/tr/td')
        
        count = 0
        tablist = []
        for x in tables:
            if count < 184:
                count += 1
                x = x.text
                tablist.append(x)
                address = tablist[1::8]
                status = tablist[3::8]


    except:
        print('could not find myTable')
    
    tablist = ['NEW MESSAGE' if item == ' NEW' else item for item in tablist]
    tablist = ['NO MESSAGE' if item == '' else item for item in tablist]

    print(len(tablist))
    print(address)
    print(status)
    print(tablist[8:16])

    driver.quit()

    end_time = time.time()
    final_time = end_time - start_time
    print(f"Run in: {final_time} seconds")

def scraper():
    start_time = time.time()
    try:
        main = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.ID, 'myTable'))
        )
        addresses = driver.find_elements(By.XPATH, '//*[@id="myTable"]/tbody/tr/td[2]')
        statuses = driver.find_elements(By.XPATH, '//*[@id="myTable"]/tbody/tr/td[4]')
        
        count_address = 0
        address = []
        for x in addresses:
            if count_address < 5:
                count_address += 1
                x = x.text.upper()
                address.append(x)
        
        count_status = 0
        status = []
        for x in statuses:
            if count_status < 5:
                count_status += 1
                x = x.text.upper()
                status.append(x)

    except:
        print('could not find myTable')
   

    print(address[0:5])
    print(status[0:5])
    print(values[1])

    print(type(address[0:5]))
    print(type(status[0:5]))
    print(type(values[1]))

    driver.quit()

    end_time = time.time()
    final_time = end_time - start_time
    print(f"Run in: {final_time} seconds")

def tester():
    address = ['630 CANADIAN GOOSE', '1927 SHOREHAM']
    status = ['RECEIVED SENT TO DG', 'COMMISSIONING VALIDATED']
    values = ['107743', '1927 SHOREHAM']

    res = []
    i = 0
    while (i < len(address)):
        if (values.count(address[i]) > 0):
            res.append(i)
        i += 1

    print(res)

def main():
    driver.minimize_window()
    driver.get(f"{url}")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, 'loginButton').click()
    scraper()

if __name__ == "__main__":
    main()