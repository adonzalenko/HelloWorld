n = int(input())
m = int(input())
t = int(input())
days = t // 1440
hours = t // 60 - 24 * days
resulthours = n + hours
resultminutes = m + (t - t // 60 * 60)
if resulthours > 24:
    resulthours = resulthours - 24
if resultminutes > 60:
    resultminutes = resultminutes - 60
    resulthours = resulthours + 1
    print(f'{resulthours:0>2}:{resultminutes:0>2}')
else:
    print(f'{resulthours:0>2}:{resultminutes:0>2}')