# Symmetric Difference
# Return all values that appear in exactly one of two collections.
# Input: [1, 2, 3], [3, 4, 5]
# Output: [1, 2, 4, 5]

def symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    result = set1.symmetric_difference(set2)

    return sorted(list(result))


# Tests
print(symmetric_difference([1, 2, 3], [3, 4, 5]))
print(symmetric_difference([1, 2], [1, 2]))
print(symmetric_difference([], [1, 2, 3]))
print(symmetric_difference([], []))


"""
Reflection:

For this challenge I wanted to use sets because the problem asks for values
that show in only one of the two places. Sets work for me for this
because they are made for comparing  values. Python also has a
symmetric_difference operation, which matches what the problem
is asking for.

The 30 minute time limit made me choose the simplest solution I cann.
Instead of using loops and always checking every value, I changed
both lists into sets and used symmetric_difference. This made the code
shorter and easier to understand. It also gave me more time to test the
program with different examples.

One trade off is that sets do not keep duplicate values, so if the input
had the same number alot of times, it would show once in the
result. For this problem that is okay because the goal is to find unique
values that only appear in one collection. I also sorted the final result
so the output is easier to read and matches the example format. I tested
normal inputs, two identical lists, an empty list, and two empty lists.
"""
