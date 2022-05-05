from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-26-ianuarie-ora-13-00/")
# table = browser.find_element_by_xpath('by=By.XPATH, value=xpath')
table = browser.find_element(by=By.XPATH, value='//*[@id="post-25198"]/div/div/table[1]/tbody')
table_text = table.text
lista = table_text.split('\n')
print(table_text)
print(lista)
header_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25198"]/div/div/table[1]/tbody/tr[1]')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
# print(dictionar)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        print(lista[i])
        dictionar[header[int(j)]].append(lista[i])
print(header)
print(table_text)
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("CazuriCovid.xls")