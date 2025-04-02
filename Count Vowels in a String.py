def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
    return sum(1 for char in s.lower() if char in vowels)

# Example usage
print(count_vowels("Apple"))  # Output: 2
