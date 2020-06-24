def is_palindrome(X):
    if X is None or X == '' or X == []:
        return False
    length = len(X)
    if length == 1:
        return True
    index = length // 2
    first_part = X[0:index]
    second_part = X[index + (length % 2):length][::-1]
    return first_part == second_part


def get_subs(s):
    n = len(s)
    masks = [1 << j for j in range(n)]
    for i in range(2 ** n):
        yield [s[j] for j in range(n) if (masks[j] & i)]


def get_longest_palindrome(X):
    lpal = ""
    for sub in get_subs(X):
        if is_palindrome(sub) and len(sub) > len(lpal):
            lpal = sub
    return ''.join(lpal)


def main():
    print(is_palindrome(None))
    print(is_palindrome(''))
    print(is_palindrome('H'))
    print(is_palindrome('ABBCABBA'))
    print(is_palindrome('AAAAAAAB'))
    print(is_palindrome('ABDFGGFDBA'))
    print(get_longest_palindrome('aezrezrezfzeraazesdfsaez'))


if __name__ == '__main__':
    main()
