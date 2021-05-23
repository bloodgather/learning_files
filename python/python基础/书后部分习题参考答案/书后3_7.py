# -*- coding: utf-8 -*-
"""

课后习题3-7

"""

# greedy

summation = 1
for i in range(1, 1000000): # (1, n) n can be very big
    summation += (-1)**(i+1) * (1 / (2 * i + 1))
    
print(summation)