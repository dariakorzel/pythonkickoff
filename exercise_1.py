# Napisac funkcje co policzy ilosc wystapien na liscie
# Przyklad

# zlicz( [1, 2, 3, 4, 1, 2, 1] )

# { 1: 3, 2: 3, 3: 1, 4: 1 }

def occurence(list):
    result = {}
    for i in list:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


occurence()
# alt shift e - run in python console
a = {'a': 1, 2: 2, '3': 3}