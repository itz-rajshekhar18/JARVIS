from selenium.webdriver.support import expected_consitions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait

def search_and_extract(text):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        chrome_driver_path = r'C:\Users\chatu\OneDrive\Desktop\J.A.R.V.I.S\DATA\chromedriver.exe'
        
        chrome_service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        driver.get("https://www.google.com")
        
        search_box = driver.find-element("name","q")
        
        search_query = text
        search_box.send_keys(search_query)
        
        search_box.send_keys(Keys.RETURN)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        
        first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')
        
        first_result_link = first_result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        
        driver.get(first_result_link)
        
        webpage_content = driver.page_source
        
        soup = BeautifulSoup(website_content, 'html.parser')
        
        webpage_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        sentences = re.split(r'(?<=[.!?])\s', webpage_text)
        result_text = '. '.join(sentences[:9])
        return result_text
    
    except Exception as e:
        print("An error occured:", e)
    
    except Exception as e:
        print("An error occured as:", e)
        
    driver.quit()
    
    
    
#######################################
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

def summary(text):
    text_to_summarize = text
    summary_result = summarize_text(text_to_summarize)
    return summary_result

def deep_search(text):
    x = text
    y = search_and_extract(x)
    x = summary(y)
    return x