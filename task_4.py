import random

original_list = [random.randint(1, 30) for _ in range(30)]
print(original_list)

non_repeating_elements = [number for number in original_list if original_list.count(number) == 1]
print(non_repeating_elements)
