def sum_numeric_values(input_list):
    """
    Sums all numeric values in a list, ignoring non-numeric items.
    
    Args:
        input_list (list): A list containing numbers and potentially other types
        
    Returns:
        float: The sum of all numeric values in the list
    """
    total = 0
    for item in input_list:
        try:
            # Try to convert to float and add to total
            total += float(item)
        except (ValueError, TypeError):
            # Skip items that can't be converted to numbers
            print(f"Skipping non-numeric item: {item}")
            continue
    return total

# Test the function with a list containing a string
test_list = [10, 20, "hello", 30, 45.5, None, 15]
print(f"Input list: {test_list}")

result = sum_numeric_values(test_list)
print(f"Sum of numeric values: {result}")

# Additional test cases
print("\n--- Additional test cases ---")

test_list_2 = [1, 2, 3, 4, 5]
print(f"Input list: {test_list_2}")
print(f"Sum: {sum_numeric_values(test_list_2)}")

test_list_3 = [10.5, 20, "string", "another string", 30.5]
print(f"Input list: {test_list_3}")
print(f"Sum: {sum_numeric_values(test_list_3)}")

test_list_4 = []
print(f"Input list: {test_list_4}")
print(f"Sum: {sum_numeric_values(test_list_4)}")

test_list_5 = ["only", "strings", "here"]
print(f"Input list: {test_list_5}")
print(f"Sum: {sum_numeric_values(test_list_5)}")