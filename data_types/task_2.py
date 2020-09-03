amount_elements = int(input('Какое количество элементов вы хотите поместить в список: '))

i = 1
list_elements = []
while amount_elements >= i:
    list_elements.append(input(f'Введите элемент {i}: '))
    i += 1
print(list_elements)

for key, _ in enumerate(list_elements[::2]):
    list_elements.insert(key*2+1, list_elements.pop(key*2))
print(list_elements)

# Не уверен, что код выше правильный с точки зрения философии python, поэтому оставил еще один закомментированным

# try:
#     key = 0
#     while key < amount_elements:
#         list_elements[key], list_elements[key + 1] = list_elements[key + 1], list_elements[key]
#         key += 2
#     print(list_elements)
# except IndexError:
#     print(list_elements)
