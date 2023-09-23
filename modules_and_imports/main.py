from package1.module1 import function_one
from package2.module2 import function_two, function_one as func_import

print(function_one())
print(function_two())
print(func_import())