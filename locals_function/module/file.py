locals_module = locals()
def ex_fn():
    print("Locals in ex_fn() function")
    print(locals())
    print("--------------------------")

    print("Print __name__ in ex_fun() function")
    print(__name__)
    print("--------------------------")

    return "Hello from module"


ex_fn()