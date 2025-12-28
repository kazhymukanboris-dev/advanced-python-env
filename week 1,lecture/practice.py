def seson(n):
    if n < 1 or n > 12:
        print("drs ailardyjaz")
        return
    if n == 1 or n ==12 or n == 2:
        print("ks")
    elif n == 3 or n == 4 or n ==5:
        print("koktem")
    elif n == 6 or n == 7 or n == 8:
        print("jaz")
    else:
         print("kz")

ai = int(input())
seson(ai)