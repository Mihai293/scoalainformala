def your_function (param, *d) :
    suma = 0
    for item in param:
        suma = suma + item
    return suma
#my_sum = your_function(1, 5, -3, "abc", [12, 56, "cad"])
print(your_function(1, 5, -3, "abc", [12, 56, "cad"]))


# def diff_vars(*params):
#     diferenta = 0
#     for item in params:
#         diferenta = diferenta - item
#     return diferenta
# print(diff_vars(1,2,3,4))