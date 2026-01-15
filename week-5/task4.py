class kizmetker:
    def __init__(self, zarplata):
        self._zarplata = zarplata

    def get_zarplata(self):
        return self._zarplata

    def get_role(self):
        return "kizmetker"


class Manager(kizmetker):
    def __init__(self, zarplata, bonus):
        super().__init__(zarplata)
        self._bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._bonus


def info_kizmetkerler(kizmetkerler):
    for e in kizmetkerler:
        print(e.get_role(), e.get_zarplata())


kizmetkerler = []

chislo_sotrudnikov = int(input("chislo sotrudnikov: "))

for i in range(chislo_sotrudnikov):
    role = input("role (kizmetker/manager): ").lower()
    zarplata = int(input("zarplata: "))

    if role == "manager":
        bonus = int(input("bonus: "))
        kizmetkerler.append(Manager(zarplata, bonus))
    else:
        kizmetkerler.append(kizmetker(zarplata))

info_kizmetkerler(kizmetkerler)
