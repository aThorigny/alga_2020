# EXERCICE 4

#
#   Question 4
#


def planning(cours):

    cours.sort() # On trie notre tableau de cours par ordre croissant

    theta = []
    duree_max = 4
    current_duree = 0

    for element in cours:
        if element + current_duree <= duree_max:
            theta.append(element)
            current_duree += element

    return theta

def main():
    cours = [3, 1.5, 2.5, 3, 0.75]
    print(planning(cours))

if __name__ == '__main__':
    main()
