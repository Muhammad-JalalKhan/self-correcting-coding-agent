def sum_strings(string_list):
    # Intentionally try to add strings without converting to int
    total = ''
    for s in string_list:
        total += s
    return total

# Test the function
result = sum_strings(['1', '2', '3'])
print(result)
# Expected output should be 6, but will get '123' instead