keys = [1, 2, 3]
values = ['one', 'two']

keys_ = [1, 2, 3]
values_ = ['one', 'two']

l1 = [1, 2, 3]
l2 = ['a','b']


def dict(k, v):
    if len(k) > len(v):
      [v.append(None) for j in range(1, len(k) - len(v) + 1)]
    return dict(map(lambda key, value: (key, value), k, v))


print(' Result#1:', dict(keys, values))
print(' Result#2:', dict(keys, values_))
print(' Result#3:', dict(l1, l2))