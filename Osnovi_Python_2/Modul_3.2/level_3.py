d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

new_d = {value: key for key, value in d.items()}

for key, value in new_d.items():
    print(key, value)
    