from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options#pt cod stabilitate browser


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.emag.ro/#opensearch")
get_element = browser.find_element(by=By.ID, value="searchboxTrigger")#accesare ID
get_element.send_keys("telefon")#scriere
get_element.submit()#enter

search_element = browser.find_element(by=By.ID, value='card_grid')
print(search_element.text)

def browser_function():#pentru pastrarea afisarii browser
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")
