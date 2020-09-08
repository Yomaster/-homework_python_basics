from functools import reduce

original_list = [number for number in range(100, 1001)]
product_elements = reduce(lambda x, y: x * y, original_list)

print(product_elements)
