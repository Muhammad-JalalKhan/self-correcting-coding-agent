# Fixed version using sum wit generator expressions 
numbers = ['5', '10', '15']
total = sum(int(n) for n in numbers)
print(f"Total: {total}")