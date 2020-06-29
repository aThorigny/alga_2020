# EXERCICE 4

#
#   Question 4
#


def planning(cours):

    cours.sort()  # On trie notre tableau de cours par ordre croissant

    planning = []
    duree_max = 4

    return planning_rec(cours, planning, duree_max)


def planning_rec(cours, planning, duree_max):

    if len(cours) == 0:
        return planning

    room = []
    to_remove = []
    current_duree = 0

    for element in cours:
            # print(element + current_duree)
        if element + current_duree <= duree_max:
            room.append(element)
            to_remove.append(element)
            current_duree += element

    if len(to_remove) > 0:
        for element in to_remove:
            cours.remove(element)

    print(len(cours))

    planning.append(room)

    return planning_rec(cours, planning, duree_max)



def main():
    cours = [ 1.5, 2.5, 3, 0.75]
    print(planning(cours))

if __name__ == '__main__':
    main()
