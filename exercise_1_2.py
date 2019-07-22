# Stworz funkcję która zwróci drugi najmniejszy element listy
# druginajmniejszy([1, 2, 3, 4, 6])
# 2


def second_smallest(my_list):
    my_list.sort()
    print(my_list[1])


second_smallest()