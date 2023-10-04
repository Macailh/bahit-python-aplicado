def custom_sum(addends=[]):
    return sum(addends)


custom_sum_lambda = lambda addends: sum(addends)

my_list = [1,2,3]

print(custom_sum(my_list))
print(custom_sum_lambda(my_list))

# Lambda sintax:
# var = lambda param_1, ..., param_n: expression

net = lambda gross, iva=16: gross + (gross * iva / 100)


print(net(1000))
print(net(1000, 19))