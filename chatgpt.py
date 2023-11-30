from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from sound_recognition import speechrecognition, speak
import pathlib
ScriptDir = pathlib.Path().absolute()

url = "https://flowgpt.com/chat"
chrome_options = Options()
chrome_options.add_argument("--headless==new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--output=/dev/null")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options= chrome_options)
driver.get(url=url)

ChatNumber =  3

def website_opener():
    while True:
        try:
            xPath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea"
            driver.find_element(by=By.XPATH , value=xPath)
            break
        except:
            pass

def checker():
    global ChatNumber
    for i in range(1,1000):
        if i % 2 !=0:
            try:
                ChatNumber = str(i)
                xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
                driver.find_element(by=By.XPATH , value=xpath)
        
            except:
                print(f"Next Chatnumber is: {i}")
                ChatNumber = str(i)
                break

def Resultscraper():
    global ChatNumber
    ChatNumber = str(ChatNumber)
    xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
    text = driver.find_element(by=By.XPATH , value=xpath).text
    ChatNumberNew = int(ChatNumber) + 2
    ChatNumber = ChatNumberNew
    return text
    
# def Popup_remover():
#     Xpath = "/html/body/div[3]/div[3]/div/section/button"
#     driver.find_element(by=By.XPATH , value=Xpath).click()
# Popup_remover()

def waitForTheAnswer():
    sleep(2)
    while True:
        try:
            xPath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/button"
            driver.find_element(by=By.XPATH , value=xPath)   
        except:
            break

def SendMessage(Query):
    xPath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea"
    driver.find_element(by=By.XPATH , value=xPath).send_keys(Query)
    sleep(0.5)
    xPath2 = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/button"
    driver.find_element(by=By.XPATH , value=xPath2).click()

website_opener()
checker()

while True:
    Query = speechrecognition()
    
    if len(str(Query))<3:
        pass
    
    elif Query== None:
        pass
    
    else:
        SendMessage(Query=Query)
        waitForTheAnswer()
        Text =Resultscraper()
        speak(Text)
        