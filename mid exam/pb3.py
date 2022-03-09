dictionar = {"1": "abc","2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}
a = dictionar.values()
list = []
while True:
    for i in a:
        for x in i:
            # print(x)
            list.append(x)
            # print(list)
    break

print(list)
# while True :
x = list[0] + list [1]
print(x)