# EXERCICE 3

#
# Question 5
#

def Lk(string):

    if len(string) == 1:
        return [0]

    stringSize = len(string)

    arrayPrefixe = [0] * stringSize

    count = 0
    i = 1

    while i < stringSize:

        if string[i] == string[count]: 
            count += 1
            arrayPrefixe[i] = count
            i += 1

        elif count > 0:
            count = arrayPrefixe[count - 1]

        else:
            arrayPrefixe[i] = count
            i += 1

    return arrayPrefixe



def main():
    print(Lk('ABABCABABABC'))
    print(Lk('MUSALANMUS'))
    print(Lk('ALANMUSALAN'))

if __name__ == '__main__':
    main()
