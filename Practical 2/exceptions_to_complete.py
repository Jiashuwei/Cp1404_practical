finished = False
# result = 0
while not finished:
    try:
        result = int(input("Enter a valid integer: "))
        finished = True
    except ValueError:
        print("please enter a valid integer.")
    print(f"valid result is: {result}")


