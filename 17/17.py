from fnmatch import *


def proizv_digit(x):
    x = str(x)
    value = 1
    for el in x:
        value *= int(el)
    return value


f = [int(x) for x in open("17-346.txt", "r")]
x = ''
cnt = 0
proizv = 0
y = []
for i in range(len(f) - 3):
    x = f[i: i + 3]
    proizv = proizv_digit(x[0]) * proizv_digit(x[1]) * proizv_digit(x[2])
    if proizv <= 2 * 10 ** 9 and fnmatch(str(proizv), '43*6*'):
        cnt += 1
        y.append(proizv)
print(cnt, max(y))
