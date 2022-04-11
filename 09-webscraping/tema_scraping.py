from bs4 import BeautifulSoup#librarie
import requests
import pandas as pd

r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
# print(r.text) #afiseaza tot codul html al paginii
link = BeautifulSoup(r.text, "html.parser") #sursa pagina(markup) + parser (ajuta asezare mai buna in pagina)
# print(link)
#div are rolul de a impartii
title = link.find_all("div", attrs={"class=entry-content"})#find all returneaza toate elementele cu clasele respective
print(title) #returneaza o lista  #tag cu atribut dictionar si elemente din code
# header = []
# dataset = []
# for i in title:#iteram prin code
#     print(i)
#     for tr_index in i.find_all("table"):#doar table pentru ca nu are clasa si nici id
#         # print(tr_index)
#         for td_index in tr_index.find_all('tr'):
#             # print(td_index)
#             td_list = []
#             if td_index.find_all('th'):
#                 header= [th_index.get_text() for th_index in td_index.find_all("th")]
#             for index, td_value in enumerate (td_index.find_all("td")):
#                 # print(index, td_value)
#                 if index == 0:
#                     td_list.append(td_value.get_text())
#                 else:
#                     td_list.append(float(td_value.get_text().replace(',', '.')))
#             dataset.append(td_list)
#
# # print(header)
# # print(dataset)
# df = pd.DataFrame(dataset, columns=header)
# print(df)
# df.to_csv("covid1.xls", header = header)