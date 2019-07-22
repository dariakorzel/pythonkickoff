# Stworz funkcję która usunie z listy najmniejszy element listy
# l = [4, 1, 2, 3]
# usun_min(l)


def delete_min(my_list):
    my_list.sort()
    my_list.pop(0)
    print(my_list)


delete_min()