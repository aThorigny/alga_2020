def is_palindrome(x: str):
    length = len(x)
    index = length // 2
    first_part = x[0:index]
    second_part = x[index + (length % 2):length][::-1]
    return first_part == second_part


print(is_palindrome("ABBBBA"))
