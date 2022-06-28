my_list = [1, 2, 3, 4, 5]

def change(x):
    return x + 10

a = list(map(change, my_list))
print(a)

####

b = list(map(lambda x: x + 10, my_list ))
print(b)

####

def func1(x):
    return x + 10

def my_map(func, list):
    res = []
    for x in list:
        res.append(func(x))
    return res

a = my_map(func1, my_list)
print(a)

###

c = my_map(func1, my_list) # Строит список
print(c)
d = list(map(func1, my_list)) # Встроенная функция - итерируемый объект => быстрее
print(d)

###

pow(4, 4) # 4 ** 4

h = list(map(pow, [1, 2, 3], [4, 5, 6]))
print(h)

###

j = list(map(func1, [1, 2, 3, 4, 5]))
print(j)

m = [func1(x) for x in [1, 2, 3, 4, 5]]
print(m)





