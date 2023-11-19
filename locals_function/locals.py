from module import file

print("Print 10")
x = 10
local_vars = locals()
print(local_vars['x'])  # Prints 10
print('------------------------------')

print("Print 42")
locals()['new_variable'] = 42
print(new_variable)  # Prints 42
print('------------------------------')

print("locals() in actual file")
print(locals())
print('------------------------------')

print("Print function ex_fn() in module file")
file.ex_fn()
# print(file.locals_module)
print('------------------------------')
