import math

friends = ['max', 'kate', 'man', 'leo']

result = []
for friend in friends:
    if friend.startswith('m'):
        result.append(friend)
# print(result)

def f(x):
    if x.startswith('m'):
        return True
    else:
        return False

result = filter(f, friends)
# print(list(result))
#
#
# print(list(filter(f, friends)))

if list(filter(f, friends)) == ['max', 'man']:
    print('Ok')
else:
    print('Failed')
assert list(filter(f, friends)) == ['max', 'man']


def f_m(f, friends):
    def f(x):
        if x.startswith('m'):
            return True
        else:
            return False
    return filter(f, friends)

# print(list(f_m(f, friends)))


print('*' * 50)


friends = ['max', 'kate', 'man', 'leo']
result = []
# for friend in friends:
#     result.append(friend.upper())
# print(result)

def f(x):
    return x.upper()
# print(list(map(f, friends)))

assert list(map(f, friends)) == ['MAX', 'KATE', 'MAN', 'LEO']

if list(map(f, friends)) == ['MAX', 'KATE', 'MAN', 'LEO']:
    print('Ok')
else:
    print('Failed')

print('*' * 50)

friends = ['max', 'kate', 'man', 'leo']

assert sorted(friends) == ['kate', 'leo', 'man', 'max']
assert sorted(friends, reverse=True) == ['max', 'man', 'leo', 'kate']

if sorted(friends) == ['kate', 'leo', 'man', 'max']:
    print('Ok')
else:
    print('Failed')

if sorted(friends, reverse=True) == ['max', 'man', 'leo', 'kate']:
    print('Ok')
else:
    print('Failed')

def test_filter():
    assert list(f_m(f, friends)) == ['max', 'man']

def test_map():
    assert list(map(f, friends)) == ['MAX', 'KATE', 'MAN', 'LEO']

def test_sorted():
    assert sorted(friends) == ['kate', 'leo', 'man', 'max']
    assert sorted(friends, reverse=True) == ['max', 'man', 'leo', 'kate']

def root(x):
    return math.sqrt(x)
print(root(4))

assert root(4) == 2.0

def test_root():
    assert root(4) == 2.0
    assert root(9) == 3.0

def func_pi(x):
    return x ** 2 * math.pi
print(func_pi(1))

assert func_pi(1) == math.pi

def test_func_pi():
    assert func_pi(1) == math.pi

def func_pow(x, y):
    return pow(x, y)
print(func_pow(3, 3))

assert func_pow(3, 3) == 27

def test_func_pow():
    assert func_pow(3, 3) == 27

def func_hypot(x, y):
    return math.hypot(x, y)
print(func_hypot(3, 4))

assert func_hypot(3, 4) == 5.0

def test_func_hypot():
    assert func_hypot(3, 4) == 5.0