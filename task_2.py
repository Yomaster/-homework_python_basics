import random

original_list = [random.randint(1, 100) for _ in range(20)]

final_list = [number for i, number in enumerate(original_list[1:], 1) if number > original_list[i-1]]
final_list1 = [original_list[i] for i in range(1, len(original_list)) if original_list[i] > original_list[i-1]]

print(original_list)
print(final_list)
print(final_list1)
