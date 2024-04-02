def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s
    # Recursive case: return the last character of the string concatenated with
    # the reverse of the substring without the last character
    return s[-1] + reverse_string(s[:-1])

# Test the function
input_string = "pots&pans"
result = reverse_string(input_string)
print("The reverse of '{}' is: {}".format(input_string, result))
