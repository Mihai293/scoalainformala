import pandas as pd

# print(pd.__version__)

# a= {'x':1, 'y':7, "z":2}
# variabila = pd.Series(a, index=['x', 'y', 'z'])#afisare pe doua randuri, keys and val
# variabila = pd.Series(a, index=a.keys())#same
# variabila = pd.Series(a, index=a.keys())#same
# print(variabila)

# data = {
#     "key1": [0, 1, 2],
#     "key2": [3, 4, 5]
# }

# variabila = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])#afisare cu denumire coloane in dataframe
# print(variabila)
# print(variabila['key2']) #valorile de pe key2, coloana
# print(variabila.loc['linie2']) #valorile de pe randul "linie2"


# df = pd.read_csv('EXEMPLU.csv')
# print(df)

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
# df=pd.DataFrame(data)#transformare din format json in data frame
# print(df)

# df = pd.read_csv("test.csv")
# print(df)
# for x in df.index:#navigare in index fisier
    # print(x)
  # print(df.loc[x, 'AL'])#afisare pe baza de index in coloana AL
  # if ':' in df.loc[x, 'AL']:
  #   df1= df.drop(x)
# print(df1.drop(x, inplace = True))
# print(df)
# df1 = df.csv('test1.csv')
# print(df.corr())
# print(df.describe())
# print(df.mean())#afiseaza media
# import matplotlib.pyplot as plt
# # df.plot(kind="scatter", x="AT", y="BE")
# df['AT'].plot(kind='hist')#histograma
# plt.show()
# print(df.head(2))#afiseaza doar primele doua randuri
# print(df.tail(3))#afiseaza ultimile 3 randuri
# new_df = df.dropna(inplace=True)#inplace modifica data frame original(inlocuieste)
# print(new_df)
# print(df.fillna(0))#inlocuieste NaN cu cifra 0
# df["AL"].fillna(0, inplace=True)#inlocuieste doar pe coloana "AL"
# print(df)
# df.loc[7, 'AL'] = 45#inlocuieste din randul 7 coloana"AL" cu 45
# print(df)
# df.replace(": ", 0, inplace=True)
# df.replace(":", 0, inplace=True)
# print(df.transpose())#intoarce tabelul(randurile devin coloane si invers)
# df.to_csv('test1.csv')#importare csv