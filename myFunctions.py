def simple_separator():
    print('*'*10)

print('simple separator')
simple_separator()

def long_separator(count):
    print('*' * count)

print('long_separator')
long_separator(15)

def separator(simbol, count):
    print()
    print(simbol * count)
    print()

print('separator')
separator('=*=',15)


def hello_world():
    for i in range(7):
        if i == 0:
            print('*' * 10)
        elif i == 3:
            print('Hello, world!')
        elif i == 6:
            print('#' * 10)
        else:
            print()

hello_world()

def hello_who(who='Julia'):
    for i in range(7):
        if i == 0:
            print('*' * 10)
        elif i == 3:
            print(f'Hello, {who}!')
        elif i == 6:
            print('#' * 10)
        else:
            print()

hello_who()

separator('=*=',15)
print('pow_many')

def pow_many(power, *args):
    n = 0
    for number in args:
        n+= number
    n **= power
    return n

print(pow_many(1, 1, 2)==3)

separator('=*=',15)
print('print_key_val')

def print_key_val(**kwargs):
    for key,value in kwargs.items():
        print(key,value)


print_key_val(name='Max', age=21)

separator('=*=',15)
print('my_filter')

def my_filter(iterable, function):
    x = list(filter(function,iterable))
    return x

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True