my_list =['string', 12, 2.4, 'other string', 45]

print('--------all list--------')
print(my_list)
print('------------------------')

print('-------for list---------')
for i in my_list:
    print(i)
print('------------------------')

print('-------first element----')
print(my_list[0])
print('------------------------')

print('------first to third----')
print(my_list[:3])
print('------------------------')

print('------add element-------')
my_list.append('new element')
print(my_list)
print('------------------------')

print('------modify element----')
my_list[0] = 'first element'
print(my_list)
print('------------------------')