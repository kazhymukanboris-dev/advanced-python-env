#checking the health of the character
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True

health = int(input("Enter health: "))
print(is_alive(health))