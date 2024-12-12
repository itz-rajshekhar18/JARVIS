from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_driver_path = r'C:\Users\chatu\OneDrive\Desktop\J.A.R.V.I.S\DATA\chromedriver.exe'

chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://www.google.com") 

def search_brain(text):
    try:
        search_box = driver.find_element("name","q")
        search_box.clear()
        
        search_query = text
        search_box.send_keys(search_query)
        
        search_box.send_keys(Keys.RETURN)
        
        driver.implicitly_wait(5)
        
        first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')
        
        first_result_text = first_result.text
        sentences = re.split(r'(?<=[.!?])\s', first_result_text)
        
        filtered_sentences = [sentence for sentence in sentences if not re.search(r'https?://\S+|(\d{1,2} [A-Za-z]+ \d{10})', sentence)]
        
        result_text = '. '.join(filtered_sentences[:10])
        result_text = result_text.replace("Featured snippet from the web","")
        return result_text
    
    except Exception as e:
        print("An error occured:", e)