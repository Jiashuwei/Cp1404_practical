try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# """Questions:"""
# TODO when will a ValueError occur?
"""When numerator and denominator are not significant numbers (they can be decimals)"""
# TODO when will a ZeroDivisionError occur?
"""When denominator is 0"""
# TODO could you change the code to avoid the possibility of a ZeroDivisionError
"""no"""