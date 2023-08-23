from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# for remote
    # capabilities = DesiredCapabilities.CHROME.copy()
    # remote_url = "http://192.168.5.55:4444/wd/hub"  # Replace with your Selenium Grid Hub URL
    # Initialize remote WebDriver
    # driver = webdriver.Remote(command_executor="http://192.168.5.55:4444/wd/hub", options=webdriver.ChromeOptions())
    # # Perform actions on the remote browser
    # driver.get("https://www.amazon.in/")




def before_all(self):
    desired_browser = self.config.userdata.get("browser")
# for initializing  different browser
    if desired_browser.lower() == "chrome":
        self.driver = webdriver.Chrome(service=Service("C:\\Users\\codoid\\Downloads\\chromedriver_win32\\chromedriver.exe"))
    elif desired_browser.lower() == "firefox":
        self.driver = webdriver.Firefox()
    elif desired_browser.lower() == "edge":
        self.driver = webdriver.Edge()
    elif desired_browser.lower() == "safari":
        self.driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {desired_browser}")
    # After browser initialized
    print("Started successfully")
    self.driver.maximize_window()
    self.driver.get("https://www.amazon.in/")
    self.driver.implicitly_wait(5)
    # for remote
    # capabilities = DesiredCapabilities.CHROME.copy()
    # remote_url = "http://192.168.5.55:4444/wd/hub"  # Replace with your Selenium Grid Hub URL
    # Initialize remote WebDriver
    # driver = webdriver.Remote(command_executor="http://192.168.5.55:4444/wd/hub", options=webdriver.ChromeOptions())
    # # Perform actions on the remote browser
    # driver.get("https://www.amazon.in/")
    
    
def after_scenario(self, driver):
    self.driver.close()
    print("Successfully")
    
    





