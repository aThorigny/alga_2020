# EXERCICE 1

#
# Question 1
#

# Dans une séquence de taille N il y a (N+1)N/2 sous-séquences  (JE CROIS QUE C'EST FAUX A REVOIR)

#
#  Question 2
#

def is_palindrome(X):

    if X is None or X == '' or X == []:
        return False

    half_length = int(len(X) / 2)

    for i in range(0, half_length):
        # on vérifie que la première partie de la string est égale à la deuxieme partie
        if X[i] != X[len(X) - i - 1]:
            return False

    return True

# Complexité de l'algorithme : Theta(n) avec n la longueur de la string en paramètre


# def is_palindrome(X):
#     if X is None or X == '' or X == []:
#         return False
#     length = len(X)
#     if length == 1:
#         return True
#     index = length // 2
#     first_part = X[0:index]
#     second_part = X[index + (length % 2):length][::-1]
#     return first_part == second_part

#
#   Question 3
#

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



#
#   Question 5
#

def get_longest_palindrome_dyn(X):
    length = len(X)

    result_array = [["" for x in range(length)] for x in range(length)]

    for sub_length in range(1, length + 1):
        for i in range(length - sub_length + 1):
            j = i + sub_length - 1
            if X[i] == X[j] and sub_length == 1:
                result_array[i][j] = X[i]
            elif X[i] == X[j] and sub_length == 2:
                result_array[i][j] = X[i]
            elif X[i] == X[j]:
                result_array[i][j] = X[i] + result_array[i + 1][j - 1] + X[i]
            else:
                l_str = result_array[i][j - 1]
                r_str = result_array[i + 1][j]
                result_array[i][j] = l_str if len(l_str) == max(len(l_str), len(r_str)) else r_str

    return result_array[0][length - 1]


def get_substr_palindrome(X):
    pass


def main():
    print(is_palindrome(None))
    print(is_palindrome(''))
    print(is_palindrome('H'))
    print(is_palindrome('ABBCABBA'))
    print(is_palindrome('AAAAAAAB'))
    print(is_palindrome('ABDFGGFDBA'))
    print(get_longest_palindrome('ALAN'))
    print(get_longest_palindrome('BANANA'))
    print(get_longest_palindrome('SOUEARRROUSRRAE'))
    print('ok')
    print(get_longest_palindrome_dyn('atezrtezeaaatsdfsttatez'))
    print(get_longest_palindrome('atezrtezeaaatsdfsttatez'))


if __name__ == '__main__':
    main()
