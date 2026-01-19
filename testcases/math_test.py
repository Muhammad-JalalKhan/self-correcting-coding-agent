# Fixed version using sum wit generator expression
numbers = ['5', '10', '15']
total = sum(int(n) for n in numbers)
print(f"Total: {total}")