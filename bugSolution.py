def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    return sum(numbers) / len(numbers)

# Example usage (this now works correctly)
average = calculate_average([])  # Passing an empty list
print(f"The average is: {average}")
average = calculate_average([1,2,3])
print(f"The average is: {average}")

# Example usage (this now works correctly)
average = calculate_average([1,2,3])  # Passing a list with numbers
print(f"The average is: {average}")