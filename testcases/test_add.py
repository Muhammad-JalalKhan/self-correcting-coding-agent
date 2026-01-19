def add(a, b):
    return a - b

result = add(5, 5)
print(result)
if result != 10:
    print("Function is incorrect, should return 10 but returned", result)
    # Fix the function
    def add(a, b):
        return a + b
    result = add(5, 5)
    print("Fixed result:", result)
    # Now it should return 10