from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def search(job_title):
    print(job_title)
    result=[]
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    profile_url = 'https://www.linkedin.com/in/yash-dwivedi-111853196/'
    # Logging into LinkedIn
    driver.get("https://linkedin.com/uas/login")
    username = driver.find_element("id", "username")
    username.send_keys("sarthakdwivedi848@gmail.com")  # Enter Your Email Address

    pword = driver.find_element("id", "password")
    pword.send_keys("Vkd@10747")  # Enter Your Password

    driver.find_element("xpath", "//button[@type='submit']").click()
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    product_search=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"search-global-typeahead__input"))
            )
    product_search.send_keys(job_title)
    product_search.send_keys(Keys.ENTER) 
    # driver.get(r'file:///C:/Users/jaink/Downloads/product%20manager%20_%20Search%20_%20LinkedIn2.html')
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    product_search_2=WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,"search-reusables__primary-filter"))
            )
    for i in product_search_2:
        if i.text=='People':
            product_search_3=i.find_element(By.XPATH, "./*")
            product_search_3.click()
            break
    # pro_0=product_search_3.find_element(By.XPATH, "./*")
    # print(product_search_3.get_attribute('outerHTML'))
    pro_10=[]
    pro_2=WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,"IynXIJkcERMknqkIsuvbNuXugAopmHgUKyLFs"))
                )

    for i in pro_2:
        pro_3=i.find_elements(By.XPATH, "./*")[1]
        pro_4=pro_3.find_element(By.XPATH, "./*")
        pro_5=pro_4.find_element(By.XPATH, "./*")
        pro_6=pro_5.find_element(By.XPATH, "./*")
        pro_7=pro_6.find_elements(By.XPATH, "./*")[0]
        pro_8=pro_7.find_element(By.XPATH, "./*")
        pro_9=pro_8.find_element(By.XPATH, "./*")
        pro_10.append(pro_9.get_attribute('href'))
    pro_11=[]
    for i in pro_10:
        pro_11.append(i.split('?')[0])

    for j in pro_11:
        mid_res=[]
        mid_res.append(job_title)
        driver.get(j)
        start = time.time()
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            initialScroll = finalScroll
            finalScroll += 1000
            time.sleep(1)
            end = time.time()
            if round(end - start) > 6:
                break


        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')

        # NAME
        name = soup.find("h1", {"class": "text-heading-xlarge inline t-24 v-align-middle break-words"})
        # CURRENT COMPANY
        company = soup.find("div", {"class": "QmNDzMMzxjZstYaxtWYTvEwvoSqRkNWkTWjs inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp inline"})
        # UNIVERSITY/COLLEGE
        university_tag = soup.find_all('span', {'class': 'visually-hidden'})
        check=0
        for i in university_tag:
            if i.text=='Education':
                check=1
            elif check==1:
                university=i.text
                break
        # CURRENT CITY 
        city = soup.find("span", {"class": "text-body-small inline t-black--light break-words"})
        if j==None:
            mid_res.append("None")
        else:
            mid_res.append(j)
        if name==None:
            mid_res.append("None")
        else:
            mid_res.append(name.get_text().strip())
        if city==None:
            mid_res.append("None")
        else:
            mid_res.append(city.get_text().strip())  
        if company==None:
            mid_res.append("None")
        else:
            mid_res.append(company.get_text().strip()) 
        if university==None:
            mid_res.append("None")
        else:
            mid_res.append(university) 
        result.append(mid_res)
    return(result)

    

