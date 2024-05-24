def building_max_number(lst: list[int]) -> int:
    lst = sorted([str(i) for i in lst], reverse=True)
    return int(''.join(lst))

lst = [56, 9, 11,2]
print(building_max_number(lst))