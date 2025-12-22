def season(number):
    if number < 1 or number > 12:
        print("durys ailardy jaz")
        return 
    
    if number == 12 or number == 1 or number == 2:
        print("kys")
    elif number == 3 or number == 4 or number == 5:
        print("koktem")
    elif number == 6 or number == 7 or number == 8:
        print("jaz")
    else:
        print("kuz")

month = int(input("enter the month: "))
season(month)