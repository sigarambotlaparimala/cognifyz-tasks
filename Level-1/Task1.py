def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

result = reverse_string("hello")
print(result)