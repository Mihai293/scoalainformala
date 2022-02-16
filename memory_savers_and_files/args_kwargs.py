# def my_function(*param_1): #returneaza tuplu
#     print(type(param_1))
#     return param_1
#
# print(my_function("string","string1","string2"))

# def numbers_sum(param1, *var): #* mereu ultima
#     suma=0
#     print(var)
#     for item in var :
#         suma = suma + item
#     return suma
# print((numbers_sum(1,2,3,4,5,)))

# def diff_vars(*params):
#     diferenta = 0
#     for item in params:
#         diferenta = diferenta - item
#     return diferenta
# print(diff_vars(1,2,3,4))

def catalog (*args, **kwargs): #returneaza dictionar

    return args, kwargs.keys()
print(catalog(1,2, nume = "Popa", prenume = "ionut", varsta = '12'))