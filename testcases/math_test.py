# Fixed version using sum with generator expression
numbers = ['5', '10', '15']
total = sum(int(n) for n in numbers)
print(f"Total: {total}")