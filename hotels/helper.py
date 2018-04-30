
FullListOfHotels = dict()
ListOfHotels = dict()
ListOfHotelsPriceToUp = dict()
ListOfHotelsPriceToDown = dict()


def setListOfHotels():
    global FullListOfHotels, ListOfHotels, ListOfHotelsPriceToDown, ListOfHotelsPriceToUp
    FullListOfHotels = {'Анапа': (('Отель 1', 2070.00, 'noimg.png'),
                                 ('Отель 2', 1700.00, 'noimg.png'),
                                 ('Отель 3', 900.00, 'noimg.png')),
                           'Адлер': (('Отель 4', 950.00, 'noimg.png'),)
                          }

    for key, value in FullListOfHotels.items():
        ListOfHotels[key] = value[0:20]

    for key1, value1 in FullListOfHotels.items():
        sorted_list =  sorted(value1, key= lambda x: x[1])
        ListOfHotelsPriceToUp[key1] = sorted_list[0:20]

    for key1, value1 in FullListOfHotels.items():
        sorted_list = sorted(value1, key= lambda x: x[1], reverse=True)
        ListOfHotelsPriceToDown[key1] = sorted_list[0:20]

    #print(ListOfHotelsPriceToDown)
