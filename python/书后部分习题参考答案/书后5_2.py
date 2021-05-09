# -*- coding: utf-8 -*-
"""

课后习题 第五章 （2）

"""

# create
scores = {
             "012": [90, 94, 97, 86, 85, 89, 88, 85],
             "005": [91, 91, 92, 98, 90, 96, 90, 95],
             "108": [96, 86, 97, 96, 87, 86, 86, 96],
             "037": [95, 95, 94, 93, 97, 98, 99, 95],
             "066": [95, 87, 94, 94, 93, 99, 96, 97],
             "020": [89, 97, 91, 95, 89, 94, 97, 92],
         }

# final is the final score
final = {}
for key, value in scores.items():
    value.sort()
    t = value[1:-1]
    final.update({key: (sum(t)/len(t))})

l = list(final.items())
# sort l with the second element
l.sort(key=lambda x:x[1], reverse=True)
final = dict(l)

print(final)