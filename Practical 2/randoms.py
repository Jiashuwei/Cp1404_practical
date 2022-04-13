import random
# line 1
print(random.randint(5, 20))
# line 2
print(random.randrange(3, 10, 2))
# line 3
print(random.uniform(2.5, 5.5))

# 1. TODO What did you see on line 1? What was the smallest number you could have seen, what was the largest?
"""I saw random integers. The smallest number I see is 5 and the largest number i see is 20"""
# 2. TODO What did you see on line 2? What was the smallest number you could have seen, what was the largest? Could line 2 have produced a 4?
"""I saw random odd numbers less than 10. The smallest number I see is 3 and the largest number I see is 9. The line 2 could not produced a 4, because they are all odd numbers"""
# 3. TODO What did you see on line 3? What was the smallest number you could have seen, what was the largest?
"""I see random decimals number greater than 2.5 but less than 5.5. The smallest number i see is 2.954... and the largest number is see is 5.472..."""
# 4. TODO Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
