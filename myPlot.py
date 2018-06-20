# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import Counter
from matplotlib import pyplot as plt

num_friends = [100, 49, 41, 40, 25, 70, 65, 72, 63, 71, 64, 60, 64, 67]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


def mean(x):
    return sum(x) / len(x)


print "mean is ", mean(num_friends)


def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2;

    if (n % 2 == 1):
        # odd
        return sorted_v[midpoint]
    else:
        # even
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


print "median is ", median(num_friends)