# discount calculator
list = {'name': 'Mound', 'height': '5.6', 'weight': '180lbs'}
print(list['name'])

while True:
    print('Enter a name : ')
    name = input()
    if name == 'mouad':
        print(list.values())  # ['Mound', '5.6', '180lbs'
        break

print(list.items())  # [('name', 'Mound'), ('height', '5.6'), ('weight', '180lbs')]
print('mouad' in list.keys())   # True or false / we can do not in too
print(list.setdefault('outfit', 'casual'))
print(list)
