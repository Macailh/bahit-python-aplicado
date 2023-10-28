def return_something(something):
    return str(something)


def call():
    something = return_something("this")
    print(something)

call()


def get_name():
    name = input("Your name: ")
    if not name:
        get_name()

get_name()