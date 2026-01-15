class Adam:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        return self._name, self._age


class Okushy(Adam):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self._sid = sid

    def info(self):
        name, age = super().info()
        return name, age, self._sid


name_a = input("adamnyn aty: ")
age_a = int(input("adamnyn jasy: "))

a = Adam(name_a, age_a)

name_o = input("okyshynyn aty: ")
age_o = int(input("okyshynyn jasy: "))
sid_o = input("ID: ")

o = Okushy(name_o, age_o, sid_o)

print(a.info())
print(o.info())
