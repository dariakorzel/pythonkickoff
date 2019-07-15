#Napisac funkcje co policzy ilosc wystapien na liscie
#Przyklad

#zlicz( [1, 2, 3, 4, 1, 2, 1] )

#{ 1: 3, 2: 3, 3: 1, 4: 1 }

def zlicz(lista):
	slownik = {}
	for i in lista:
		if i in slownik:
			slownik[i] = slownik[i] + 1
		else:
			slownik[i] = 1
	return slownik
zlicz()