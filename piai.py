from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from sound_recognition import speechrecognition
import pathlib
ScriptDir = pathlib.Path().absolute()

url = "https://pi.ai/talk"
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

sleep(3)
VoiceIsOnOrOff = False

def VoiceOnButton():
    global VoiceIsOnOroff
    Xpath = '/html/body/div/main/div/div/div[3]/div[3]/div/div[2]/button'
    driver.find_element(by=By.XPATH,value=Xpath).click()
    VoiceIsOnOroff = True
   

def QuerySender(QUERY):
    XpathInput = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea"
    XpathSenderButton = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button"
    driver.find_element(by=By.XPATH, value=XpathInput).send_keys(QUERY)
    sleep(1)
    driver.find_element(by=By.XPATH, value= XpathSenderButton).click()
    sleep(1)

def wait_for_result():
    sleep(1)
    XpathInput = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea"
    driver.find_element(by=By.XPATH, value=XpathInput).send_keys("waiting...")
    sleep(1)
    button = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button"
    while True:
        try:
            btn = driver.find_element(by=By.XPATH, value=button).is_enabled()
            if btn == True:
                driver.find_element(by=By.XPATH, value=XpathInput).clear()
                break
            else:
                pass
        except:
            pass
            
def result():
    text = driver.find_element(by=By.XPATH, value= "/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]").text
    return text

def is_audio_playing():
        script = """
        var audio = document.querySelector("audio");
        return !audio.paused && audio.currentTime > 0 && !audio.ended && audio.readyState > 2;
        """
        return driver.execute_script(script)

def MainExecution():  
        Query = speechrecognition()
        if len(str(Query))<3:
            pass
        
        elif Query== None:
            pass
        
        else:
            QuerySender(QUERY = Query)
            global VoiceIsOnOrOff
            if VoiceIsOnOrOff == False:
                VoiceOnButton()
                VoiceIsOnOrOff = True
            else:
                pass   
            
            wait_for_result()
            
            print("")
            print(f"==> Pi AI : {result()}")
            print("")
            while is_audio_playing():
                sleep(1)
        
    
        
while True:
    MainExecution()
        