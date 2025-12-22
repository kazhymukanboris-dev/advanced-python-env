def season_events(number_of_month):
    if number_of_month < 1 or number_of_month > 12:
        print("You need to enter the real number of the month")
        return

    if number_of_month == 12 or number_of_month == 1 or number_of_month == 2:
        print("You were born in Winter. White snow fell outside the window.")
    elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
        print("You were born in Spring. Birds sang beautiful songs.")
    elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8:
        print("You were born in Summer. The sun shone brighter than ever.")
    else:
        print("You were born in Autumn. The harvest was incredible.")

month = int(input("Enter month number: "))
season_events(month)
